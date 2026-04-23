from weasyprint import HTML, CSS
import os

def convert_html_to_a4_pdf(html_file):
    if not os.path.exists(html_file):
        print(f"파일을 찾을 수 없습니다: {html_file}")
        return

    output_pdf = html_file.replace(".html", ".pdf")
    
    # A4 출력을 위한 최적의 인쇄 스타일 정의
    print_style = """
    @page {
        size: A4;
        margin: 5mm; /* 사방 여백 */
    }
    body {
        font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
        font-size: 10.5pt; /* 일반적인 문서용 글자 크기 */
        line-height: 1.6;
        color: #000;
    }
    h1 { font-size: 18pt; margin-top: 30pt; margin-bottom: 20pt; border-bottom: 2pt solid #000; }
    h2 { font-size: 14pt; margin-top: 25pt; border-bottom: 1pt solid #ccc; }
    h3 { font-size: 12pt; margin-top: 20pt; color: #333; }
    p, li { font-size: 10.5pt; margin-bottom: 10pt; }
    
    /* 목차 컨테이너가 페이지 중간에 잘리지 않도록 설정 */
    .toc-container { 
        page-break-inside: avoid; 
        background: #f0f0f0 !important; 
        border: 1pt solid #ccc !important;
    }
    
    /* 섹션이 바뀔 때 가급적 새 페이지에서 시작 */
    section { page-break-before: always; }
    h1, h2, h3 { page-break-after: avoid; } /* 제목이 페이지 끝에 홀로 남지 않게 함 */
    """

    print(f"PDF 생성 중: {output_pdf}...")
    
    try:
        # HTML 파일 로드 및 PDF 저장
        HTML(filename=html_file).write_pdf(
            output_pdf,
            stylesheets=[CSS(string=print_style)]
        )
        print(f"성공: {output_pdf} 파일이 생성되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    # 변환할 파일 리스트 (TOC가 포함된 최신 파일 권장)
    target_files = ["Unity_Privacy_EN_with_TOC.html", "Unity_Privacy_KO_with_TOC.html"]
    
    for html in target_files:
        convert_html_to_a4_pdf(html)