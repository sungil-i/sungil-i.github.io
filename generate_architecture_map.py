import os
import ast
import re

def get_python_docstring(filepath):
    """파이썬 파일의 최상단 주석(Docstring)을 추출합니다."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        node = ast.parse(content)
        doc = ast.get_docstring(node)
        if doc:
            lines = [line.strip() for line in doc.split('\n') if line.strip()]
            return lines[0] if lines else None
    except Exception:
        pass
    return None

def get_astro_summary(filepath):
    """Astro 파일의 프론트매터 주석이나 HTML 주석을 추출합니다."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 프론트매터(--- ... ---) 내부의 한 줄 주석(//) 추출
        frontmatter_match = re.search(r'^---\s*(.*?)\s*---', content, re.DOTALL | re.MULTILINE)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            for line in frontmatter.split('\n'):
                stripped = line.strip()
                if stripped.startswith('//'):
                    return stripped.lstrip('/').strip()
        
        # 2. HTML 주석(<!-- -->) 추출
        html_comment_match = re.search(r'<!--(.*?)-->', content, re.DOTALL)
        if html_comment_match:
            lines = [line.strip() for line in html_comment_match.group(1).split('\n') if line.strip()]
            return lines[0] if lines else None
            
    except Exception:
        pass
    return None

def get_markdown_summary(filepath):
    """마크다운 파일의 프론트매터 title이나 최상위 헤딩(#)을 추출합니다."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. 프론트매터의 title: "..." 추출
        title_match = re.search(r'^title:\s*[\'"]?([^\'"\n]+)[\'"]?', content, re.MULTILINE)
        if title_match:
            return f"문서: {title_match.group(1).strip()}"
            
        # 2. 최상위 헤딩(# 제목) 추출
        heading_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
        if heading_match:
            return f"문서: {heading_match.group(1).strip()}"
            
    except Exception:
        pass
    return None

def get_js_ts_summary(filepath):
    """JS/TS 파일의 최상단 한 줄 주석(//)을 추출합니다."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith('//'):
                    return stripped.lstrip('/').strip()
                # 코드가 시작되면 중단
                if stripped and not stripped.startswith('import') and not stripped.startswith('/*'):
                    break
    except Exception:
        pass
    return None

def get_file_summary(filepath, ext):
    """확장자에 맞는 파싱 함수를 호출하여 요약을 반환합니다."""
    desc = None
    if ext == '.py':
        desc = get_python_docstring(filepath)
    elif ext == '.astro':
        desc = get_astro_summary(filepath)
    elif ext in ['.md', '.mdx']:
        desc = get_markdown_summary(filepath)
    elif ext in ['.js', '.ts', '.mjs', '.cjs']:
        desc = get_js_ts_summary(filepath)
        
    return desc if desc else "역할을 요약해주세요."

def generate_map(root_dir='.', output_file='architecture_map_draft.md'):
    # 스캔에서 제외할 불필요한 폴더 (Astro 캐시 폴더 .astro 추가)
    ignore_dirs = {
        '.git', '__pycache__', 'node_modules', 'venv', '.venv', 'env', 
        '.svelte-kit', 'build', 'dist', '.vercel', 'logs', 'datas',
        'backup_old_version', 'demo', '4_Archives', 'koreainvest_csv', 'docs',
        '.astro'
    }
    # 스캔에서 제외할 자산 파일 확장자
    ignore_exts = {
        '.pyc', '.pyo', '.pyd', '.db', '.sqlite', '.sqlite3', '.gz', 
        '.csv', '.xlsx', '.png', '.jpg', '.jpeg', '.log', '.svg', '.gif', '.webp'
    }
    
    # 아키텍처 맵에 포함할 대상 확장자
    target_exts = {'.py', '.sh', '.js', '.ts', '.mjs', '.cjs', '.astro', '.md', '.mdx', '.json'}

    tree_lines = ["### 1. 디렉토리 구조 (Tree)"]
    module_lines = ["### 2. 모듈별 한 줄 요약"]

    print("🔍 Astro 프로젝트 디렉토리 스캔을 시작합니다...")

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
            ext = os.path.splitext(f)[1].lower()
            if ext in ignore_exts:
                continue
            
            filepath = os.path.join(dirpath, f)
            tree_lines.append(f"{subindent}- {f}")

            # 타겟 확장자일 경우 모듈 요약 추가
            if ext in target_exts:
                if ext == '.json':
                    desc = "설정 파일 및 정적 데이터"
                elif ext == '.sh':
                    desc = "쉘 스크립트"
                else:
                    desc = get_file_summary(filepath, ext)
                    
                # Astro는 컴포넌트 명이 겹치는 경우가 많아 상대 경로 전체를 출력
                rel_path = os.path.relpath(filepath, root_dir)
                module_lines.append(f"- `{rel_path}` : {desc}")

    # 데이터 흐름 가이드 추가
    pipeline_str = "### 3. 데이터 흐름 (Astro Pipeline)\n- **마크다운 문서** (`src/pages/`) ➔ 레이아웃 컴포넌트 (`MainLayout.astro`, `PostLayout.astro` 등) 통과 ➔ 빌드(`npm run build`) ➔ 정적 사이트 호스팅\n"

    # 최종 마크다운 조합
    final_content = f"# 🗺️ UPJ Architecture Map (Draft)\n\n"
    final_content += "\n".join(tree_lines) + "\n\n"
    final_content += "\n".join(module_lines) + "\n\n"
    final_content += pipeline_str

    # 파일 쓰기
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print(f"✅ 프로젝트 지도의 초안이 [{output_file}]에 성공적으로 저장되었습니다!")
    print("💡 터미널에서 'cat architecture_map_draft.md' 명령어로 확인하시거나,")
    print("   내용을 복사하여 참참이에게 보내주시면 함께 완벽하게 다듬어 나가겠습니다.")

if __name__ == "__main__":
    generate_map()