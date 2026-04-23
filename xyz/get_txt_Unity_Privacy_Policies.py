import requests
from bs4 import BeautifulSoup

def fetch_unity_legal_text(urls):
    """
    주어진 URL 리스트를 순회하며 본문 텍스트를 추출하는 함수
    """
    # 웹사이트에서 로봇으로 인식하여 차단하는 것을 방지하기 위한 헤더 설정
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    all_texts = ""
    
    for url in urls:
        print(f"데이터를 가져오는 중입니다: {url}")
        try:
            # 1. 페이지 요청
            response = requests.get(url, headers=headers)
            response.raise_for_status() # 에러 발생 시 예외 처리
            
            # 2. HTML 파싱
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 유니티 사이트의 본문이 주로 위치하는 <main> 태그 탐색, 없으면 <body> 전체 사용
            content_area = soup.find('main') or soup.body
            
            if content_area:
                # 문서 구분을 위한 구분선 및 URL 추가
                all_texts += f"\n\n{'='*80}\n"
                all_texts += f"DOCUMENT URL: {url}\n"
                all_texts += f"{'='*80}\n\n"
                
                # 3. 메뉴나 푸터 등을 제외하고, 의미 있는 텍스트를 담은 주요 태그만 필터링
                for element in content_area.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'li']):
                    text = element.get_text(strip=True)
                    if text:
                        all_texts += text + "\n\n"
                        
        except Exception as e:
            print(f"오류 발생 ({url}): {e}")
            
    return all_texts

if __name__ == "__main__":
    # 추출할 12개의 유니티 개인정보처리방침 관련 링크 목록
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
    
    # 텍스트 추출 실행
    result_text = fetch_unity_legal_text(target_urls)
    
    # 4. 추출된 데이터를 하나의 텍스트 파일로 통합 저장
    output_filename = "Unity_Privacy_Policies.txt"
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(result_text)
        
    print(f"\n모든 문서 추출이 완료되었습니다! 현재 폴더의 '{output_filename}' 파일을 확인해 주세요.")