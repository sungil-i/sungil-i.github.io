import os
from bs4 import BeautifulSoup

def add_toc_to_html(filename):
    if not os.path.exists(filename):
        print(f"파일을 찾을 수 없습니다: {filename}")
        return

    with open(filename, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # 1. 목차를 구성할 H 태그(H1, H2, H3) 추출
    header_tags = soup.find_all(['h1', 'h2', 'h3'])
    
    toc_html = '<div class="toc-container">\n<h2>목차 (Table of Contents)</h2>\n<ul>\n'
    
    for i, tag in enumerate(header_tags):
        # 태그에 ID가 없으면 고유 ID 부여 (이동 링크용)
        tag_id = tag.get('id')
        if not tag_id:
            tag_id = f"heading-{i}"
            tag['id'] = tag_id
        
        # 태그 레벨에 따른 들여쓰기 결정
        indent_class = f"toc-{tag.name.lower()}"
        toc_html += f'    <li class="{indent_class}"><a href="#{tag_id}">{tag.get_text()}</a></li>\n'
    
    toc_html += '</ul>\n</div>\n<hr>\n'

    # 2. 목차 스타일(CSS) 추가
    style_tag = soup.find('style')
    if style_tag:
        toc_css = """
        .toc-container { background: #f8f9fa; border: 1px solid #ddd; padding: 20px; margin-bottom: 30px; border-radius: 8px; }
        .toc-container ul { list-style: none; padding-left: 0; }
        .toc-container a { text-decoration: none; color: #0366d6; }
        .toc-container a:hover { text-decoration: underline; }
        .toc-h1 { font-weight: bold; margin-top: 10px; }
        .toc-h2 { margin-left: 20px; font-size: 0.95em; }
        .toc-h3 { margin-left: 40px; font-size: 0.9em; color: #666; }
        """
        style_tag.append(toc_css)

    # 3. <body> 태그 바로 아래에 목차 삽입
    if soup.body:
        # 기존 내용의 가장 앞에 목차 추가
        soup.body.insert(0, BeautifulSoup(toc_html, 'html.parser'))

    # 4. 파일 저장 (기존 파일명에 _v2를 붙여 저장하거나 덮어쓰기)
    new_filename = filename.replace(".html", "_with_TOC.html")
    with open(new_filename, "w", encoding="utf-8") as f:
        f.write(soup.prettify())
    
    print(f"성공: 목차가 추가된 파일이 생성되었습니다 -> {new_filename}")

if __name__ == "__main__":
    # 처리할 파일 리스트
    files_to_process = ["Unity_Privacy_EN.html", "Unity_Privacy_KO.html"]
    
    for file in files_to_process:
        add_toc_to_html(file)