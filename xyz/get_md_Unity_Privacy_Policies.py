import requests
from bs4 import BeautifulSoup
import re

def fetch_to_markdown(urls):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    md_content = "# Unity Legal & Privacy Policy Documents\n\n"
    md_content += "> 통합 생성일: 2026-04-23\n\n---\n"
    
    for url in urls:
        print(f"Processing: {url}")
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 1. 문서 제목 추출 (h1)
            title = soup.find('h1')
            title_text = title.get_text(strip=True) if title else url.split('/')[-1].replace('-', ' ').title()
            
            md_content += f"\n# {title_text}\n\n"
            md_content += f"**Source URL:** [{url}]({url})\n\n"
            
            # 2. 본문 영역 탐색
            content_area = soup.find('main') or soup.body
            
            if content_area:
                # 불필요한 스크립트나 스타일 제거
                for s in content_area(['script', 'style', 'nav', 'footer']):
                    s.decompose()

                # 주요 태그들을 마크다운 형식으로 변환
                for element in content_area.find_all(['h2', 'h3', 'h4', 'p', 'li']):
                    tag = element.name
                    text = element.get_text(strip=True)
                    
                    if not text: continue
                    
                    if tag == 'h2':
                        md_content += f"## {text}\n\n"
                    elif tag == 'h3':
                        md_content += f"### {text}\n\n"
                    elif tag == 'h4':
                        md_content += f"#### {text}\n\n"
                    elif tag == 'p':
                        md_content += f"{text}\n\n"
                    elif tag == 'li':
                        md_content += f"* {text}\n"
                
                md_content += "\n---\n" # 문서 간 구분선
                        
        except Exception as e:
            md_content += f"\n# Error fetching {url}\n\n{str(e)}\n\n---\n"
            
    return md_content

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
    
    final_md = fetch_to_markdown(target_urls)
    
    with open("Unity_Privacy_Policies.md", "w", encoding="utf-8") as f:
        f.write(final_md)
        
    print("\n'Unity_Privacy_Policies.md' 파일 생성이 완료되었습니다.")