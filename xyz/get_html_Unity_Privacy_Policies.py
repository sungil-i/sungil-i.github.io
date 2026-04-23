import requests
from bs4 import BeautifulSoup

def fetch_to_html(urls):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # HTML 헤더 및 CSS 스타일 정의
    html_start = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unity Legal & Privacy Policy Documents</title>
    <style>
        :root { --primary-color: #222; --link-color: #0366d6; --bg-color: #f6f8fa; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 40px 20px; background-color: #fff; }
        h1 { border-bottom: 2px solid #eaecef; padding-bottom: 10px; color: var(--primary-color); margin-top: 50px; }
        h2 { border-bottom: 1px solid #eaecef; padding-bottom: 5px; margin-top: 35px; color: #444; }
        h3 { margin-top: 25px; color: #555; }
        p { margin: 15px 0; text-align: justify; }
        ul { background: var(--bg-color); padding: 20px 40px; border-radius: 8px; }
        li { margin-bottom: 10px; }
        code { background: #f0f0f0; padding: 2px 5px; border-radius: 4px; font-family: 'Consolas', monospace; }
        .source-link { font-size: 0.9em; color: var(--link-color); text-decoration: none; }
        .source-link:hover { text-decoration: underline; }
        .timestamp { color: #888; font-style: italic; margin-bottom: 30px; }
        hr { border: 0; height: 1px; background: #eee; margin: 40px 0; }
        .nav-box { background: #f9f9f9; padding: 20px; border-left: 4px solid #ccc; margin-bottom: 40px; }
    </style>
</head>
<body>
    <h1>Unity Legal & Privacy Policy Documents</h1>
    <p class="timestamp">통합 생성일: 2026-04-23</p>
    <div class="nav-box"><strong>Quick Navigation:</strong> <ul id="toc"></ul></div>
"""
    
    html_body = ""
    toc_items = "" # 목차용 데이터
    
    for i, url in enumerate(urls):
        print(f"Processing: {url}")
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 1. 문서 제목 추출 및 ID 부여 (목차용)
            title = soup.find('h1')
            title_text = title.get_text(strip=True) if title else url.split('/')[-1].replace('-', ' ').title()
            doc_id = f"doc-{i}"
            
            toc_items += f'<li><a href="#{doc_id}">{title_text}</a></li>'
            
            html_body += f'<section id="{doc_id}">\n'
            html_body += f'<h1>{title_text}</h1>\n'
            html_body += f'<p><strong>Source:</strong> <a href="{url}" class="source-link" target="_blank">{url}</a></p>\n'
            
            content_area = soup.find('main') or soup.body
            if content_area:
                for s in content_area(['script', 'style', 'nav', 'footer', 'iframe']):
                    s.decompose()

                # HTML 태그를 그대로 유지하며 필요한 태그만 추출
                for element in content_area.find_all(['h2', 'h3', 'h4', 'p', 'li']):
                    tag = element.name
                    # 클래스나 스타일 속성을 제거하여 깔끔하게 만듦
                    clean_element = soup.new_tag(tag)
                    clean_element.string = element.get_text(strip=True)
                    
                    if clean_element.string:
                        html_body += str(clean_element) + "\n"
            
            html_body += '<hr></section>\n'
                        
        except Exception as e:
            html_body += f'<section><h1>Error fetching {url}</h1><p>{str(e)}</p><hr></section>\n'
            
    html_end = """
    <script>
        // 목차 동적 삽입
        document.getElementById('toc').innerHTML = `""" + toc_items + """`;
    </script>
</body>
</html>"""
    
    return html_start + html_body + html_end

if __name__ == "__main__":
    target_urls = [
        "https://unity.com/kr/legal/privacy-policy",
        "https://unity.com/legal/developer-privacy-policy",
        "https://unity.com/legal/developer-privacy-policy-faq",
        "https://unity.com/legal/game-player-and-app-user-privacy-policy",
        "https://unity.com/legal/game-player-and-app-user-privacy-faq",
        "https://unity.com/legal/educational-products-for-schools-privacy-notice",
        "https://unity.com/legal/privacy-supplement-statement-for-unity-mars-companion-app",
        "https://unity.com/legal/unity-data-processing-addendum-dpa",
        "https://unity.com/legal/dpa-amendment-eu-uk-swiss-sccs",
        "https://unity.com/legal/technical-and-organisational-measures",
        "https://unity.com/legal/subprocessors",
        "https://unity.com/legal/supplemental-privacy-statement-unity-muse"
    ]
    
    final_html = fetch_to_html(target_urls)
    
    with open("Unity_Privacy_Policies.html", "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print("\n'Unity_Privacy_Policies.html' 파일 생성이 완료되었습니다. 브라우저로 확인해 보세요!")