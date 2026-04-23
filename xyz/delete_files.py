import subprocess
import concurrent.futures

# 🎓 원준님의 실습실 PC 공통 아이디와 비밀번호를 입력해주세요!
STUDENT_ID = "User"   # 예: Administrator, User, Student 등
STUDENT_PW = "1234"   # 실제 비밀번호 (비밀번호가 아예 없다면 "" 빈칸으로 두세요)

def delete_files_with_auth(ip):
    # 비밀번호를 윈도우 보안 문자열로 변환하고 신분증($cred)을 만드는 파워셸 명령어
    ps_cmd = (
        f"$pwd = ConvertTo-SecureString '{STUDENT_PW}' -AsPlainText -Force; "
        f"$cred = New-Object System.Management.Automation.PSCredential ('{STUDENT_ID}', $pwd); "
        f"Invoke-Command -ComputerName {ip} -Credential $cred -ScriptBlock {{ "
        f"Remove-Item -Path 'C:\\Users\\User\\Documents\\EnableWinRM.bat', 'C:\\Users\\User\\Desktop\\EnableWinRM.bat' -Force -ErrorAction SilentlyContinue; "
        f"Write-Output 'Clean' }}"
    )
    
    cmd = ["powershell.exe", "-NoProfile", "-Command", ps_cmd]
    
    try:
        # cp949 인코딩으로 한글 깨짐 방지
        output = subprocess.check_output(cmd, text=True, encoding='cp949', stderr=subprocess.STDOUT)
        
        if "Clean" in output:
            return f"✅ [{ip}] 인증 통과 및 파일 삭제 성공!"
        else:
            return f"➖ [{ip}] 인증 통과 (지울 파일이 이미 없습니다)"
            
    except subprocess.CalledProcessError as e:
        error_msg = e.output.strip().split('\n')[0]
        return f"❌ [{ip}] 상세 에러: {error_msg}"

if __name__ == "__main__":
    print("--- 🚀 실습실 26대 인증 강제 돌파 및 정리 시작 ---")
    
    base_ip = "10.104.145."
    ips = [f"{base_ip}{i}" for i in range(201, 227)]

    # 26대 동시 타격
    with concurrent.futures.ThreadPoolExecutor(max_workers=26) as executor:
        results = executor.map(delete_files_with_auth, ips)

    for res in results:
        print(res)
        
    print("--- ✨ 실습실 청소 작전 완료! ---")