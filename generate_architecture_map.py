import os
import ast

def get_docstring(filepath):
    """파이썬 파일의 최상단 주석(Docstring)을 추출하여 한 줄 요약으로 반환합니다."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        node = ast.parse(content)
        doc = ast.get_docstring(node)
        if doc:
            # 주석 중 비어있지 않은 첫 번째 줄만 추출
            lines = [line.strip() for line in doc.split('\n') if line.strip()]
            return lines[0] if lines else ""
    except Exception:
        pass
    return "역할을 요약해주세요."

def generate_map(root_dir='.', output_file='architecture_map_draft.md'):
    # 스캔에서 제외할 불필요한 폴더 및 확장자 (AI 컨텍스트 절약용)
    ignore_dirs = {
        # '.git', '__pycache__', 'node_modules', 'venv', '.venv', 'env', 
        # '.svelte-kit', 'build', 'dist', '.vercel', 'logs', 'datas',
        # 'backup_old_version', 'demo', '4_Archives', 'koreainvest_csv'
        # 'docs'
    }
    ignore_exts = {
        '.pyc', '.pyo', '.pyd', '.db', '.sqlite', '.sqlite3', '.gz', 
        '.csv', '.xlsx', '.png', '.jpg', '.jpeg', '.json', '.log'
    }

    tree_lines = ["### 1. 디렉토리 구조 (Tree)"]
    module_lines = ["### 2. 모듈별 한 줄 요약"]

    print("🔍 프로젝트 디렉토리 스캔을 시작합니다...")

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # 숨김 폴더 및 무시할 폴더 제외
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs and not d.startswith('.')]

        level = dirpath.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        basename = os.path.basename(dirpath)

        if level == 0:
            tree_lines.append(f"- ./ (Project Root)")
        else:
            tree_lines.append(f"{indent}- {basename}/")

        subindent = ' ' * 4 * (level + 1)
        for f in sorted(filenames):
            if f.startswith('.'): # 숨김 파일 제외 (.env 등)
                continue
            ext = os.path.splitext(f)[1]
            if ext in ignore_exts:
                continue
            
            filepath = os.path.join(dirpath, f)
            tree_lines.append(f"{subindent}- {f}")

            # 파이썬, 쉘, JS/TS 파일만 모듈 요약에 추가
            if ext in ['.py', '.sh', '.js', '.ts']:
                desc = get_docstring(filepath) if ext == '.py' else "역할을 요약해주세요."
                module_lines.append(f"- `{f}` : {desc}")

    # pipeline_str = "### 3. 데이터 흐름 (Pipeline)\n- 브로커 ➔ live_sync ➔ worker ➔ DB ➔ frontend\n"

    # 최종 마크다운 조합
    final_content = f"# 🗺️ UPJ Architecture Map (Draft)\n\n"
    final_content += "\n".join(tree_lines) + "\n\n"
    final_content += "\n".join(module_lines) + "\n\n"
    # final_content += pipeline_str

    # 파일 쓰기
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print(f"✅ 프로젝트 지도의 초안이 [{output_file}]에 성공적으로 저장되었습니다!")
    print("💡 터미널에서 'cat architecture_map_draft.md' 명령어로 확인하시거나,")
    print("   내용을 복사하여 참참이에게 보내주시면 함께 완벽하게 다듬어 나가겠습니다.")

if __name__ == "__main__":
    generate_map()