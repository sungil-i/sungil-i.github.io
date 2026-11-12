### File: backend/v2/chamcham-chloe/sync_to_drive.py
"""
참참(ChamCham, AI 아키텍트)과 클로(Chloe, Claude REPL 코딩 어시스턴트)가
동일한 프로젝트 컨텍스트(아키텍처/스키마/API/상태 문서)를 Google Drive를 통해
실시간으로 공유하기 위한 단방향(local -> Drive) 동기화 스크립트입니다.

실행 방법 (CLAUDE.md의 conda run 패턴 준수):
    & "<CONDA_EXE_PATH>" run -n "<CONDA_ENV_NAME>" python chamcham-chloe\\sync_to_drive.py
"""

import os
import random
import socket
import sys
import time
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# chamcham-chloe/ 의 부모 = backend/v2 (프로젝트 루트)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

# Google Drive 파일 전체 읽기/쓰기 권한 스코프 (업데이트를 위해 drive.file 대신 drive 사용)
_DRIVE_SCOPES = ["https://www.googleapis.com/auth/drive"]
_MIME_TYPE_MARKDOWN = "text/markdown"
# NotebookLM이 원본 .md 파일을 인식하지 못해 업로드 대상 mimeType을
# Google Docs로 강제 변환한다. 로컬 파일 자체는 여전히 text/markdown으로 읽어 전송하고,
# Drive API가 이 값을 보고 마크다운을 Docs 포맷으로 자동 파싱한다(커스텀 파싱 불필요).
_MIME_TYPE_GOOGLE_DOC = "application/vnd.google-apps.document"

# 참참<->클로가 실시간 공유할 3개 컨텍스트 문서 (모두 프로젝트 루트 기준)
# database_schema.md / api_registry.md는 제외한다: 이 프로젝트는 정적 마크다운
# 기반 Astro 사이트로 DB나 백엔드 API가 존재하지 않는다.
SYNC_FILES = [
    "architecture_map.md",
    "CLAUDE.md",
    "system_state.md",
]

# [Requirement 29] Drive API가 일시적으로 반환하는 재시도 가능한 HTTP 상태 코드.
_TRANSIENT_HTTP_STATUS_CODES = {500, 502, 503, 504, 429}
# 소켓/연결 단절 계열 예외도 동일하게 일시적 오류로 취급한다 (네트워크 순단 등).
_TRANSIENT_SOCKET_EXCEPTIONS = (
    ConnectionResetError,
    ConnectionAbortedError,
    ConnectionError,
    BrokenPipeError,
    socket.timeout,
    TimeoutError,
)


def retry_drive_api_call(api_call_fn, max_retries=5, initial_delay=2.0, backoff_factor=2.0):
    """
    [Requirement 29] Google Drive API 호출(주로 요청 객체의 `.execute()`)을 감싸,
    일시적 오류(HTTP 500/502/503/504/429, 소켓 연결 끊김/리셋/타임아웃)에 한해
    지수 백오프 + 지터(random.uniform(0.5, 1.5))로 재시도한다.

    `api_call_fn`은 인자 없이 즉시 실행 가능한 콜러블이어야 한다
    (예: `lambda: service.files().list(...).execute()`). 일시적이지 않은
    오류(예: 403 권한 오류, 404)는 즉시 재-raise하여 불필요한 재시도를 하지 않는다.
    `max_retries`회를 모두 소진하면 원인 오류를 그대로 raise하므로, 호출부
    (`upload_file`/`sync_all` 등)가 해당 항목만 건너뛰고 나머지 SYNC_FILES
    처리를 이어갈 수 있다 - 로컬 파일은 이 스크립트가 읽기만 하므로 이 경로에서
    로컬 상태가 훼손될 일은 없다.
    """
    delay = initial_delay
    last_error: Optional[BaseException] = None

    for attempt in range(1, max_retries + 1):
        try:
            return api_call_fn()
        except HttpError as exc:
            status = exc.resp.status if getattr(exc, "resp", None) is not None else None
            if status not in _TRANSIENT_HTTP_STATUS_CODES:
                raise
            label = str(status)
            last_error = exc
        except _TRANSIENT_SOCKET_EXCEPTIONS as exc:
            label = type(exc).__name__
            last_error = exc

        if attempt >= max_retries:
            print(
                f"[ERROR] Drive API 호출이 {max_retries}회 재시도 후에도 실패했습니다 "
                f"(마지막 오류: {label}). 이 항목은 건너뛰고 다음 항목을 계속 처리합니다."
            )
            raise last_error

        wait_seconds = delay + random.uniform(0.5, 1.5)
        print(
            f"[WARNING] Drive API transient error {label} detected. "
            f"Retrying in {wait_seconds:.2f}s (Attempt {attempt}/{max_retries})..."
        )
        time.sleep(wait_seconds)
        delay *= backoff_factor


def _get_drive_service():
    """
    .env의 GDRIVE_FOLDER_ID / GCP_SERVICE_ACCOUNT_JSON을 읽어 Drive v3 서비스
    객체와 대상 폴더 ID를 반환합니다. 서비스 계정 키 파일이 아직 준비되지 않은
    경우(placeholder 단계) 명확한 에러 메시지와 함께 조기 실패시킵니다.
    """
    folder_id = os.getenv("GDRIVE_FOLDER_ID")
    creds_relpath = os.getenv("GCP_SERVICE_ACCOUNT_JSON")
    if not folder_id or not creds_relpath:
        raise RuntimeError(
            "GDRIVE_FOLDER_ID / GCP_SERVICE_ACCOUNT_JSON이 .env에 설정되어 있지 않습니다."
        )

    creds_file = PROJECT_ROOT / creds_relpath
    if not creds_file.exists():
        raise FileNotFoundError(
            f"서비스 계정 키 파일을 찾을 수 없습니다: {creds_file}\n"
            "GCP 콘솔에서 Drive API용 서비스 계정 JSON 키를 발급받아 이 경로에 저장하세요."
        )

    credentials = service_account.Credentials.from_service_account_file(
        str(creds_file), scopes=_DRIVE_SCOPES
    )
    service = build("drive", "v3", credentials=credentials, cache_discovery=False)
    return service, folder_id


def find_existing_file_id(service, remote_name: str, folder_id: str) -> Optional[str]:
    """
    대상 폴더 내에서 trashed=false 상태의 동일 파일명을 검색합니다.
    기존 파일이 있으면 그 fileId를 재사용해 update()로 덮어써서 영구 공유 링크가
    깨지지 않도록 합니다 (요구사항: trashed=false 쿼리로 삭제된 파일 오검색 방지).
    """
    escaped_name = remote_name.replace("'", "\\'")
    query = f"name = '{escaped_name}' and '{folder_id}' in parents and trashed = false"
    response = retry_drive_api_call(
        lambda: service.files()
        .list(q=query, spaces="drive", fields="files(id, name)", pageSize=1)
        .execute()
    )
    files = response.get("files", [])
    return files[0]["id"] if files else None


def upload_file(service, local_path: Path, remote_name: str, folder_id: str) -> str:
    """
    파일이 이미 존재하면 update(), 없으면 create()로 업로드하고 fileId를 반환합니다.
    대상 파일은 항상 Google Docs(application/vnd.google-apps.document)로
    생성/유지됩니다. 업로드되는 미디어의 mimetype은 text/markdown 그대로 두어, Drive API가
    마크다운 텍스트를 Docs 포맷으로 자동 변환하도록 합니다. update() 호출 시에는 대상
    파일이 이미 Google Docs 파일(사전 생성된 backend_v2-* 빈 문서)이므로 mimeType을 다시
    지정할 필요가 없습니다 - Drive는 기존 파일의 mimeType을 유지한 채 콘텐츠만 변환합니다.
    """
    media = MediaFileUpload(str(local_path), mimetype=_MIME_TYPE_MARKDOWN, resumable=False)
    existing_id = find_existing_file_id(service, remote_name, folder_id)

    if existing_id:
        retry_drive_api_call(
            lambda: service.files().update(fileId=existing_id, media_body=media).execute()
        )
        return existing_id

    created = retry_drive_api_call(
        lambda: service.files()
        .create(
            body={
                "name": remote_name,
                "parents": [folder_id],
                "mimeType": _MIME_TYPE_GOOGLE_DOC,
            },
            media_body=media,
            fields="id",
        )
        .execute()
    )
    return created["id"]


def build_remote_name(local_filename: str, prefix: str) -> str:
    """PROJECT_PREFIX(.env)를 파일명 앞에 동적으로 붙입니다 (하드코딩 금지).
    Drive 상의 대상 Google Docs 파일은 확장자 없이 명명되어 있으므로
    (예: backend_v2-architecture_map), 로컬 .md 확장자는 제거한 뒤 접두사를 붙인다.
    이를 생략하면 find_existing_file_id()가 기존 Docs를 찾지 못해 매번 create()로
    빠지고, 마크다운 소스는 Docs로 변환되지 않은 채 신규 중복 파일만 쌓이게 된다.
    """
    stem = Path(local_filename).stem
    return f"{prefix}{stem}"


def sync_all() -> dict:
    """
    SYNC_FILES에 정의된 5개 문서를 순회하며 존재하는 파일만 Google Drive로
    업로드/갱신합니다. 존재하지 않는 파일은 조용히 건너뜁니다(하드 실패 방지).
    """
    service, folder_id = _get_drive_service()
    # ✨ .env 파싱 시 붙는 trailing whitespace/개행(\r\n, \n)이
    # 그대로 파일명 접두사에 섞이면 Drive 상 파일명이 미묘하게 어긋나(trashed=false 검색
    # 실패 -> 매번 create() 시도 -> storageQuotaExceeded) 재현하기 어려운 버그가 되므로
    # 반드시 strip()으로 정제한 뒤에만 접두사로 사용한다.
    prefix = os.getenv("PROJECT_PREFIX", "").strip()

    results = {}
    for filename in SYNC_FILES:
        local_path = PROJECT_ROOT / filename
        if not local_path.exists():
            print(f"[SKIP] {filename} 파일이 없어 건너뜁니다.")
            continue

        remote_name = build_remote_name(filename, prefix)
        try:
            file_id = upload_file(service, local_path, remote_name, folder_id)
        except Exception as exc:
            # [Requirement 29] 재시도(retry_drive_api_call)를 모두 소진한 뒤에도
            # 실패하면 이 파일만 건너뛰고 나머지 SYNC_FILES 동기화를 계속 진행한다.
            # 로컬 파일은 읽기 전용으로만 접근하므로 로컬 상태 훼손 위험은 없다.
            print(f"[ERROR] {filename} -> {remote_name} 동기화 실패, 건너뜁니다: {exc}")
            continue
        results[remote_name] = file_id
        print(f"[OK] {filename} -> {remote_name} (fileId={file_id})")

    return results


def sync_single_file(relative_path: str, remote_name_override: Optional[str] = None) -> Optional[str]:
    """[Requirement 13, 2026-08-06] SYNC_FILES(5개 핵심 문서 전용, CLAUDE.md
    ChamCham-Chloe Context Sync 규칙 대상)의 자동 동기화 범위를 넓히지 않으면서,
    임의의 단일 파일(예: references/UPJ_Trading_System_Session_Section_Table.md)을
    1회성으로 같은 Drive 폴더에 동기화하고 싶을 때 쓰는 헬퍼. sync_all()/SYNC_FILES는
    전혀 건드리지 않는다 - 5개 핵심 문서의 "매 세션 자동 동기화" 계약은 그대로다.

    ✨ [Requirement 14 Task 1, 2026-08-06] remote_name_override - 5개 핵심 문서는
    PROJECT_PREFIX(예: "backend_v2-")가 붙은 이름으로 Drive에 존재하지만, 이
    파일(UPJ_Trading_System_Session_Section_Table)은 접두사 없이 정확히 그
    이름으로 이미 Drive에 존재한다(과제 원문 확인). build_remote_name()의 기본
    접두사 규칙을 그대로 적용하면 find_existing_file_id()가 그 기존 파일을 찾지
    못해 매번 새 파일 create()를 시도하다 storageQuotaExceeded로 실패한다 -
    override를 넘기면 그 정확한 이름으로 검색/갱신한다."""
    local_path = PROJECT_ROOT / relative_path
    if not local_path.exists():
        print(f"[SKIP] {relative_path} 파일이 없어 건너뜁니다.")
        return None

    service, folder_id = _get_drive_service()
    if remote_name_override is not None:
        remote_name = remote_name_override
    else:
        prefix = os.getenv("PROJECT_PREFIX", "").strip()
        remote_name = build_remote_name(relative_path, prefix)
    file_id = upload_file(service, local_path, remote_name, folder_id)
    print(f"[OK] {relative_path} -> {remote_name} (fileId={file_id})")
    return file_id


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            sync_single_file(sys.argv[1], remote_name_override=sys.argv[2] if len(sys.argv) > 2 else None)
        else:
            sync_all()
    except Exception as exc:
        print(f"[ERROR] Google Drive 동기화 실패: {exc}", file=sys.stderr)
        sys.exit(1)
