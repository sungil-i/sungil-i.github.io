---
layout: ../../../../layouts/PostLayout.astro
title: "정기고사 2 준비"
date: "2026-06-09"
---

# 정기고사 학습내용

## C# 첫걸음 1

### 1. 간단한 인사말 출력

Java의 System.out.println과 1:1로 대응되는 가장 기본 문장입니다.

주의사항

- 대/소문자를 구분합니다.
- 닷(.), 큰따옴표("), 세미콜론(;)을 정확히 입력해야 합니다.

```csharp
Console.WriteLine("Hello 시샵 C#");
```

### 2. 변수(이름 상자) 만들기

```csharp
string myname = "김성일";
Console.WriteLine(myname);
```

### 3. 두 단어 합치기

연산자를 사용해서 두 단어를 합칠 수 있습니다.

```csharp
string myhome = "용인";
Console.WriteLine("나는 "+ myhome + "에 살고 있습니다.");
```

### 4. 변수(숫자 상자) 만들기

```csharp
int ban = 10;
Console.WriteLine("나는 " + ban + "반입니다.");
```

### 5. 간단한 덧셈 계산

```csharp
int apple = 5;
int grape = 3;
Console.WriteLine("과일의 총 개수는 "+ (apple+grape) +" 개입니다.");
```

## C# 첫걸음 2

### 1. 사용자에게 이름 물어보기

> ReadLine ↔ WriteLine

```csharp
string input = Console.ReadLine();
Console.WriteLine(input + "님, 안녕하세요.");
```

### 2. 내가 좋아하는 숫자

```csharp
string favNumber = Console.ReadLine();
Console.WriteLine("내가 좋아하는 숫자: " + favNumber);
```

### 3. 여러 줄 출력하기

① 첫번째 방법 (일반적인 방법 )

```csharp
Console.WriteLine("첫번째 줄");
Console.WriteLine("두번째 줄");
Console.WriteLine("세번째 줄");
```

② 두번째 방법 (특수 기호 넣기 \\n)

```csharp
Console.WriteLine("첫번째 줄\n두번째 줄\n세번째 줄");
```

③ 세번째 방법 (문자열 리터럴 사용 @)

```csharp
Console.WriteLine(@"첫번째 줄
두번째 줄
세번째 줄");
```

### 4. 현대적인 출력 방식 ($)

```csharp
string myname = "김성일";
Console.WriteLine($"나의 이름은 {myname} 입니다.");
```

### 5. 프로그램 멈춰 세우기

프로그램이 실행 직후 바로 꺼지는 것을 방지하는 필수 명령어입니다.

```csharp
Console.ReadKey();
```

## 2.변수와 연산자

### (1)-1. 정수형 변수 활용하기

- 플레이어의 레벨(int)을 15로 선언하세요.
- 게임 서버 전체 사용자의 총 경험치(long)를 9000억으로 선언하세요. (900000000000L)

```csharp
int level = 15;
long totalExp = 9000000000000L;
Console.WriteLine($"레벨: {level}, 총 경험치: {totalExp}");
```

### (1)-2. 소수점 데이터 다루기

- 원주율(float)을 3.14로 선언하세요. (f 접미사 활용)
- 아주 정밀한 물리 상수(double)를 0.0000000123으로 선언하세요.

```csharp
float pi = 3.14f;
double physic = 0.00000000123;
Console.Write($"파이: {pi}, 더블변수: {physic}");
```

### (1)-3. 텍스트 데이터 선언하기

- 아이템 등급(char)을 'S'로 선언하세요.
- 아이템 이름(string)을 "전설의 검"으로 선언하세요.

> **char 은 문자 1개: 작은따옴표(')**
> **string 은 문자열: 큰따옴표(")**

```csharp
char itemGrade = 'S';
string itemName = "전설의 검";
Console.WriteLine($"[{itemGrade}] {itemName}");
```

### (1)-4. 논리형 데이터

> 논리형 데이터: 참/거짓 판별할 때 쓰이는 변수 (자바의 boolean 과 동일함)

- 퀘스트 완료 여부(bool: 불)를 true로 선언하세요.
- 로그인 중인지 여부(bool: 불)를 false로 선언하세요.

```csharp
bool isQuestComplete = true;
bool isLogin = false;
Console.WriteLine($"퀘스트 완료: {isQuestComplete}");
Console.WriteLine($"로그인 중: {isLogin}");
```

### (1)-5. 변수 값 업데이트

> 기존 변수를 선언한 뒤 새로운 값을 할당할 수 있습니다.

- int gold = 1000;
- gold 변수의 값을 1500으로 변경하고 출력하세요.

```csharp
int gold = 1000;
// 아이템 획득.. 코인 획득.. (+500)
gold = 1500;
Console.WriteLine($"현재 골드: {gold}");
```

### (2)-1. 산술 연산자

- int maxHp = 100;
- int damage = 35;
- maxHp에서 damage를 뺀 결과를 currentHp(int)에 저장하세요.
- currentHp를 출력하세요.

| 종류 | 연산자 |
|:-:| :-: |
| 더하기 | + |
| 빼기 |- |
| 곱하기 | * |
| 나누기 | / |
| 나머지 | % |
| 증가 연산자 | ++ |
| 감소 연산자 | -- |

```csharp
int maxHp = 100;
int damage = 35;
int currentHp = maxHp - damage;
currentHp = currentHp + 10;
Console.WriteLine($"현재 체력: {currentHp}");
```

### (2)-2. 비교, 논리 연산자

- 비교 연산자( >, <, >=, <=, == )
- 논리 연산자( AND &&, OR ||, NOT ! )

**AND 연산자**

| A | B | **A && B** |
| :-: | :-: | :-: |
| 참(true) | 참(true) | **참(true)** |
| 참(true) | 거짓(false) | **거짓(false)** |
| 거짓(false) |참(true) | **거짓(false)** |
| 거짓(false)| 거짓(false) | **거짓(false)** |


**AND 연산자 사용 예시**

> 레벨이 20 이상이고( && )<br>티켓을 가지고 있는지 여부를<br>canEnter(bool)에 저장하세요. <br>
> 그리고 canEnter를 출력하세요.

```csharp
int level = 25;
bool hasTicket = true;
bool canEnter = (level >= 20) && (hasTicket == true);
Console.WriteLine($"입장 가능 여부: {canEnter}");
```



**OR 연산자**

| A | B | **A \|\| B** |
| :-: | :-: | :-: |
| 참(true) | 참(true) | **참(true)** |
| 참(true) | 거짓(false) | **참(true)** |
| 거짓(false) | 참(true) | **참(true)** |
| 거짓(false) | 거짓(false) | **거짓(false)** |



**OR 연산자 사용 예시**

> 레벨이 20 이상거나( || )<br>티켓을 가지고 거나 할 때 입장 가능하다.<br>canEnter(bool)에 저장하세요. <br>
> 그리고 canEnter를 출력하세요.

```csharp
int level = 25;
bool hasTicket = true;
bool canEnter = (level >= 20) || (hasTicket == true);
Console.WriteLine($"입장 가능 여부: {canEnter}");
```

### (2)-3. 복합 대입 연산자

- += : 덧셈 복합 대입 연산자 
- -= : 뺄셈 복합 대입 연산자
- *= : 곱셈 복합 대입 연산자
- /= : 나눗셈 복합 대입 연산자

```csharp
int a = 10;
a += 30; // 같은표현 a = a + 30; 
```

> int exp = 500;<br>
> 복합 대입 연산자를 사용하여 exp에 250을 더하세요.<br>
> 결과값을 출력하세요.

```csharp
int exp = 500;
exp += 250; // 같은 표현 exp = exp + 250;
Console.WriteLine($"현재 경험치: {exp}");
```

### (2)-4. 문자열 함수: 포함 여부 확인

> string inventory = "물약, 열쇠, 지도";<br>
> 1. inventory 문자열에 "열쇠"가 포함되어 있는지 확인하여 결과(bool)를 출력하세요.

string 객체의 **Contains** 함수를 사용하면, 문자열에 원하는 문자가 포함되어 있는지 확인할 수 있습니다.

```csharp
string inventory = "물약, 열쇠, 지도";
bool hasWord = inventory.Contains("열쇠");
Console.WriteLine(hasWord);
```

### (2)-5. 문자열 함수: 바꾸기

string 객체의 **Replace** 함수는 특정 문자를 내가 원하는 문자로 바꿔주는 역할을 합니다.

사용법

**word.Replace("ABC", "DEF");**
**: word 에서 "ABC" 라는 문자를 찾아서 "DEF"로 바꿔줍니다.**

> string rawMessage = "오늘은 정말 우울한 날이야.";<br>
> "우울한" → "멋진"<br>
> 으로 문자열을 바꾸시오.

```csharp
string rawMessage = "오늘은 정말 우울한 날이야.";
string newMessage = rawMessage.Replace("우울한", "멋진");
Console.WriteLine(rawMessage);
Console.WriteLine(newMessage);
```

## 3. 조건문

### (1)-1. 단일 if문

문법 형식

```csharp
// 조건 이 참(true) 일때 코드을 실행합니다.
// 조건 은 bool형 자료가 들어갑니다.
if( 조건 ) {
    코드
}
```

**예시**

> 현재 체력(hp)이 50 미만일 때만<br>"포션을 사용합니다."를 출력하는<br>기본 if문을 작성합니다.

```csharp
int hp = 30;
bool is_ok = hp < 50;
if( is_ok ) {
    Console.WriteLine("포션을 사용합니다.");
}
```

### (1)-2. if-else (양자택일)

조건에 맞게 둘중 하나를 선택하는 구문입니다.

문법 형식

```csharp
// 조건이 참(true)일 때 코드1을 실행하고
// 조건이 거짓(false)일 때 코드2를 실행합니다.
if(조건) {
    코드1
} else {
    코드2
}
```

**예시**

> 점수(score)가 60점 이상이면 "합격",<br>아니면 "불합격"을 출력합니다.

```csharp
int score = 75;
bool is_pass = score >= 60;
if( is_pass ) {
    Console.WriteLine("합격");
} else {
    Console.WriteLine("불합격");
}
```

### (1)-3. else if문 (다중 조건)

> 여러개의 조건을 다룰 수 있다.

**예시**

> 레벨(Level)에 따라 등급을 나눈다.<br>◎ 9이상: "전설"<br>◎ 5이상: "영웅"<br>◎ 나머지: "일반

```csharp
int level = 7;
if( level >= 9 ) {
    Console.WriteLine("전설 등급");
} else if ( level >= 5 ) {
    Console.WriteLine("영웅 등급");
} else {
    Console.WriteLine("일반 등급");
}
```

### (1)-4. 중첩 조건

> if문 속에 if문이 있는 형태입니다.

**예시**

> 레벨이 20 이상이면서<br>입장권(hasTicket)이 true 일때만<br>입장이 가능하다.

```csharp
int level = 25;
bool hasTicket = true;
if( level >= 20 ) {
    if( hasTicket ) {
        Console.WriteLine("입장 가능!!");
    }
}
```

### (1)-5. 논리 연산자를 활용한 조건문

**예시1 (AND)**

> 마나(mp)가 10 이상이고<br>거리가 5 이내일 때<br>"공격!"을 출력합니다.

```csharp
int mp = 15;
int distance = 3;
if( (mp >= 10) && (distance <= 5) ) {
    Console.WriteLine("공격!");
}
```

**예시2 (NOT)**

> 티켓이 없을 때, "경고" 메시지를 출력합니다.

NOT(!) 연산자는 반대로 바뀝니다.<br>
!참 → 거짓<br>
!거짓 → 참

```csharp
bool hasTicket = false;
if( !hasTicket ) {
    Console.WriteLine("경고");
}
```

### (1)-6. 삼항 연산자

> if문을 한줄로 나타낸 형태

**문법**

```csharp
// 조건이 참이면, 변수에 A를 넣고
// 조건이 거짓이면, 변수에 B를 넣어라.
변수 = (조건) ? A : B
```

**예시**

> 24시간 기반의 시간이 주어지고 AM 또는 PM 를 설정하라

```csharp
int time24h = 15;
string timeTxt = (time24h >= 12) ? "PM" : "AM";
Console.WriteLine($"{time24h}시는 {timeTxt} 입니다.");
```

결과

```text
15시는 PM 입니다.
```

## 4. 반복문

> 반복문과 친해지기 (for, while)

**게임이 돌아가는 원리**

이미지를 초당 x번씩 화면에 보여줍니다.<br>
code: 반복문(while)을 사용해서 서로 다른 이미지를<br>
일정 간격으로 화면에 뿌려준다.

- Start: 처음 화면
- Update: 움직이는 화면

### (1)-1. 1부터 5까지 숫자 세기 (for문)

**문법**

```csharp
// 시작값 ~ 끝나는 조건까지, 단계에 따라
// 코드를 반복해서 실행한다.
for( 시작값; 끝나는 조건; 단계 ) {
    코드;
}
```

예시

> for문을 사용하여 1부터 5까지 숫자를 순서대로 출력하기

```csharp
for(int i=1; i<=5; i=i+1) {
    Console.WriteLine($"{i}번째 반복");
}
```

실행결과

```text
1번째 반복
2번째 반복
3번째 반복
4번째 반복
5번째 반복
```

### (1)-2. 카운트 다운 (while문)

**문법**

조건이 참(true)일 동안 코드를 반복합니다.<br>
while 문은 조건에 따라 무한 반복할 수 있습니다.

```csharp
while(조건) {
    코드;
}
```

예시

> while문을 사용하여 3부터 1까지 <br>숫자를 거꾸로 줄여가며 카운트다운을 합니다.

```csharp
int count = 3;
while(count > 0) {
    Console.WriteLine($"카운트 다운: {count}");
    count = count - 1;
}
```

실행결과

```text
카운트 다운: 3
카운트 다운: 2
카운트 다운: 1
```

### (1)-3. 짝수만 건너뛰기 (continue)

continue 를 만나면<br>아래 코드를 무시하고 **다음 반복**으로 넘어갑니다.

예시

> 1부터 5까지 반복하다가,<br>i가 3일 때는 continue를 사용해 건너뛰세요.

```csharp
for(int i=1; i<=5; i=i+1) {
    if(i == 3) {
        continue;
    }
    Console.WriteLine($"{i}번째 반복");
}
```

실행결과

```text
1번째 반복
2번째 반복
4번째 반복
5번째 반복
```

### (1)-4. 반복문 멈추기 (break)

break 문은 반복문을 강제 종료합니다.

예시

> 1부터 5까지 탐색하다가<br>4에서 break를 사용해 탐색을 멈추세요.

```csharp
for(int i=1; i<=5; i=i+1) {
    if(i == 4) {
        break;
    }
    Console.WriteLine($"{i}번째 반복");
}
```

실행결과

```text
1번째 반복
2번째 반복
3번째 반복
```

### (1)-5. 구구단 출력하기

실습예제

> for문을 사용해서 dan 변수에 구구단의 단을 넣고<br>구구단을 출력하세요.

```csharp
int dan = 2;
for(int i=1; i<=9; i=i+1) {
    Console.WriteLine($"{dan}x{i}={dan*i}");
}
```

실행결과

```text
2x1=2
2x2=4
2x3=6
2x4=8
2x5=10
2x6=12
2x7=14
2x8=16
2x9=18
```

### (2)-1. 반복해서 생성하기 (for문)

> 유니티에서 적을 여러 마리 생성(Spawning)할 때 사용하는 기초 로직입니다.

예제

for문을 사용해서 적을 3개 생성하세요.

```csharp
for(int i=1; i<=3; i++) { // i=i+1
    Console.WriteLine($"{i}번째 적을 생성했습니다.");
}
```

### (2)-2. 체력 물약 마시기 (while문)

예시

> 인벤토리에 있는 물약을 모두 소모할 때까지 체력을 회복하는 로직입니다.

```csharp
int potion = 3;
while(potion > 0) {
    Console.WriteLine("${potion}번째 체력 물약 소진");
    potion--;     // potion = potion - 1
}
Console.WriteLine("물약 없음");
```

### (2)-3. 아이템 건너뛰기 (continue)

> 특정 아이템(3번째)을 건너뛰게 합니다.

```csharp
for(int i=1; i<=5; i++) {
    if(i==3) continue;
    Console.Write($"{i}번째 아이템 줍기");
}
```

### (2)-4. 적 생성 종료 (break)

예시

> 적 생성 도중 특정 아이템 발생 시 생성 종료하기

```csharp
int enemy = 1;
while(true) {    
    Console.Write($"{enemy}번째 적 생성");
    if(enemy==10) break;
    enemy++;
}
```

### (2)-5. 구구단 만들기 (while문 사용)

> while 문을 사용해서 구구단 7단을 완성하시오.

```csharp
int dan = 7;
int i = 1;
while(i<=9) {
    Console.WriteLine(i);
    i++;
}
```

## 5. 조건문과 반복문 응용

- 변수와 연산자
- 조건문(if-else) + 반복문(for, while, continue, break)

### (1)-1.구구단의 특정 단 출력하기

예시 (코드 명세서)

> 숫자(몇단)를 입력 받습니다.<br>for문과 if을 사용해서 입력된 단의 구구단을 완성한다.<br>입력 받은 수가 2~9 사이가 아닐 경우 경고 메시지를 출력한다.

```csharp
string a = Console.ReadLine(); // 문자열
int dan = int.Parse( a ); // 문자열 → 정수
if( dan >= 2  &&  dan <= 9 ) {
    for(int i=1; i<=9; i++) {
        Console.WriteLine($"{dan} x {i} = {dan*i}");
    }
} else {
    Console.WriteLine("입력오류!");
}
```

결과 예시

```text
> 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
```

### (1)-2. 1부터 N까지 짝수의 합 구하기

> 1.숫자(N)를 입력받는다.<br>2.While 문을 사용해서 N까지 짝수의 합을 더한다.

**i % 2 == 0  →  i는 짝수이다.**

**i % 2 == 1  →  i는 홀수이다.**

```csharp
int n = int.Parse( Console.ReadLine() );
int i = 1;
int total = 0;
while ( i <= n  ) {
    if(i%2 == 0) total = total + i; // total += i; 와 같은 표현
    i++;
}
Console.WriteLine($"total = {total}");
```

실행 결과

```text
> 100
total = 2550
```

### (1)-3. 3-6-9 게임

> 게임규칙:<br>1부터 N 까지 반복해서<br>3,6,9가 들어가면 "짝" 출력<br>아니면 숫자 출력하기<br>(예)<br>13 → "짝"<br>60 → "짝"

```csharp
int n = int.Parse( Console.ReadLine() );
for(int i=1; i <= n; i++) {
    string str = i.ToString();
    if(
        str.Contains("3") ||
        str.Contains("6") ||
        str.Contains("9")
    ) Console.WriteLine("짝");
    else Console.WriteLine(str);
}
```

실행결과

```text
> 10
1
2
짝
4
5
짝
7
8
짝
10
```

### (1)-4. 비밀번호 맞추기 (3회 제한)

> 로그인 창에서 아이디와 비밀번호를 입력할 때<br>비밀번호를 3번만에 맞춰야 한다.<br>그렇지 않으면 에러 메시지를 출력한다.

```csharp
// (구현 로직)
// 1.입력한 비밀번호가 맞는지 체크한다.
// 2.비밀번호가 맞으면 is_ok = true 로 바꾼다.
// 3.비밀번호가 맞으면 for문을 빠져나온다.
// 4.비밀번호가 틀리면 계속 for문을 반복한다.

string password = "sungil";
bool is_ok = false;
for(int i=1; i<=3; i++) {
    Console.Write("비밀번호를 입력하세요: ");
    if(Console.ReadLine() == password) {
        is_ok = true;
        break;
    }
}
Console.WriteLine(is_ok ? "SUCCESS" : "FAIL");
```

### (1)-5. 0입력 시 종료 및 합계 산출

> 숫자를 무한히 입력 받는다.<br>문자열을 숫자로 바꿔서 계속 더한다.<br>0이 나오면 반복문을 빠져나오고,<br>지금까지 입력한 모든 숫자의 합을 출력한다.

```csharp
int total = 0;
while(true) {
    int num = int.Parse( Console.ReadLine() );
    Console.WriteLine($"입력한 숫자={num}");
    if(num == 0) break;
    // total = total + num;
    total += num;
}
Console.WriteLine($"total={total}");
```

## 6. 배열

> 배열은 같은 자료형이 연속적으로 저장된 형태입니다.

**정수형 배열**

```csharp
int[] numbers = {1, 2, 3, 4, 5};
```

**(주의) 배열의 인덱스는 0부터 시작합니다.**

### 1-(1). 문자열 배열

```csharp
string[] words = {"A", "B", "C", "D", "E"};
Console.WriteLine(words[0]);
Console.WriteLine(words[4]);
string myword = "ABCDE";
Console.WriteLine(myword[0]);
Console.WriteLine(myword[4]);
```

실행 결과

```text
A
E
A
E
```

### 1-(2). 배열의 값 수정하기

처음 배열을 만들 때 넣은 값은 나중에 다른 값으로 바꿀 수 있습니다.

```csharp
int[] scores = {10, 20, 30, 40, 50};
Console.WriteLine(scores[2]);
scores[2] = 99;
Console.WriteLine(scores[2]);
```

실행 결과

```text
30
99
```

### 1-(3). 배열의 길이(Length) 알아내기

배열 안에 데이터가 몇개나 들어 있는지 일일이 셀 필요가 없습니다.<br>**.Length** 라는 속성을 사용하면 배열 전체의 길이를 알려줍니다.

```csharp
int[] numbers = {2, 4, 6, 8, 10, 12};
Console.WriteLine($"배열의 크기={numbers.Length}");
for(int i=0; i<numbers.Length; i++) {
    Console.WriteLine($"{numbers[i]}");
}
```

실행 결과

```text
배열의 크기=6
2
4
6
8
10
12
```

### 1-(4). 배열을 꺼꾸로 출력하기

for문을 사용해서 배열을 꺼꾸로 출력할 수 있습니다.

```csharp
int[] numbers = {2, 4, 6, 8, 10, 12};
for(int i=numbers.Length-1; i>=0; i--) {
    Console.WriteLine($"{i}인덱스의 값={numbers[i]}");
}
```

실행 결과

```text
5인덱스의 값=12
4인덱스의 값=10
3인덱스의 값=8
2인덱스의 값=6
1인덱스의 값=4
0인덱스의 값=2
```

## 7. 프로그래밍 언어 개요

### 1. 프로그래밍 언어의 분류

#### 1. 개발 편의성 측면에 따른 분류

* **저급 언어:** 기계어, 어셈블리어
* **고급 언어:** C, C++, C#, Python,  등 대다수 언어

#### 2. 실행 및 구현 방식에 따른 분류

* **명령형 언어:** 컴퓨터에 저장된 명령어들이 순차적으로 실행되는 프로그래밍 방식으로 상태를 강조하는 언어이다.
* **함수형 언어:** 함수의 응용을 강조하여 수학적인 수식 등의 함수들로 프로그램을 구성하여 호출하는 방식의 언어이다.
* **논리형 언어:** 논리적인 문장 구조를 이용하여 프로그램을 표현하고 계산을 수행하는 구조로 추론과 관계 규칙에 의해 원하는 결과를 얻는 언어이다.
* **객체지향형 언어:** 객체 간의 관계에 초점을 두고 기능을 중심으로 메소드를 구현하는 방법으로 상속, 캡슐화, 다형성, 추상화 등의 특징을 갖고 있다.

#### 3. 빌드(Build) 방식에 따른 언어 분류

작성한 소스코드가 컴퓨터에서 실행 가능한 형태로 변하는 과정을 빌드(Build)라고 하며, 이 방식에 따라 언어를 세 가지로 나눌 수 있습니다.

* **컴파일 언어 (Compile Language)**
    * **특징:** 소스코드가 기계어 실행 파일로 통째로 빌드되는 방식입니다. 번역 속도는 걸리지만, 한 번 번역되면 **실행 속도가 매우 빠릅니다.**
    * **종류:** C, C++, C#


* **인터프리터 언어 (Interpreter Language)**
    * **특징:** 소스코드를 미리 번역하지 않고, 실행할 때 **한 줄씩 번역하며 실행**하는 방식입니다. **실시간 실행 및 결과 분석**에 유리합니다.
    * **종류:** Python 등


* **바이트 코드 언어 (Byte Code Language)**
    * **특징:** 컴파일을 통해 1차적으로 가상머신(Virtual Machine)이 이해할 수 있는 **Byte Code**로 변환한 뒤, 가상머신이 각 운영체제(Native OS)에 맞춰 다시 기계어로 번역해 실행하는 방식입니다.
    * **종류:** JAVA, Scala 등


### 2. 개발 목적 및 분야별 프로그래밍 언어 분류

소프트웨어를 개발할 때는 개발하는 대상과 플랫폼에 따라 사용하는 언어가 완전히 상이합니다.

* **인공지능/데이터 분석:** Python, R
* **프런트엔드 (사용자 화면):** HTML, CSS, JavaScript
* **백엔드/웹 서비스:** JSP, PHP, ASP 등
* **모바일 개발 (Mobile)**
* **안드로이드(Android):** JAVA, Kotlin 등
* **iOS (아이폰):** Objective-C, Swift 등
* **데스크톱 (Desktop):** C, C++, C# 등
* **게임 (Game):** C, C++, Unity(C#) 등
* **AI / 빅데이터 분석:** Python, R 등

## 8. 유니티

### 1. C# 언어와 유니티(Unity) 엔진의 관계

* **C# 언어의 정의:** C와 C++의 발전된 형태로 마이크로소프트의 **.NET 환경**에 맞춰 설계된 언어입니다. 사용자 인터페이스(UI)를 쉽게 만들 수 있는 **컴포넌트 기능**을 기본 제공합니다.
* **유니티(Unity) 엔진:** 단순한 언어가 아니라 그래픽 처리, 물리 연산, 사운드 등 게임 필수 시스템을 미리 갖춘 종합 게임 엔진(개발 환경)입니다. 유니티에서 게임의 규칙과 로직을 짜는 주력 스크립트 언어가 바로 C#입니다.
* **멀티 플랫폼(Multi-platform) 빌드의 이점:** 유니티 내에서 **하나의 C# 소스 코드**만 작성해 두면, 안드로이드(.apk), iOS, PC(.exe), 콘솔 등 다양한 기기용 파일로 한 번에 추출할 수 있습니다. 각 OS별 언어(Java, Swift 등)를 따로 배울 필요가 없어 시간과 비용이 절약됩니다.

<!-- 
<br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br>
 -->
### 2. 유니티 화면 구성

![유니티 화면 구성](unity_gui.jpg)

* **1. 씬 뷰 (Scene View)**
    * **특징:** 개발자가 게임 월드를 직접 보면서 캐릭터나 배경 등 **오브젝트를 배치, 이동, 회전, 크기 조절하는 작업 공간**입니다. 플레이어에게는 보이지 않는 개발자 전용 설계도 화면입니다.

* **2. 게임 뷰 (Game View)**
    * **특징:** 게임이 실행되었을 때 **플레이어가 실제로 보게 될 최종 화면**을 미리 보여주는 창입니다. 씬에 배치된 '카메라(Camera)'가 비추는 화면을 그대로 출력하며, 상단의 Play(▶) 버튼을 누르면 실시간으로 게임을 테스트할 수 있습니다.

* **3. 하이어라키 창 (Hierarchy Window)**
    * **특징:** 현재 열려 있는 씬에 **배치되어 있는 모든 게임 오브젝트들을 리스트 형태의 계층 구조(부모-자식 관계)로 나열**해 주는 창입니다. 이곳에 이름이 존재해야만 현재 게임 세상에 존재하는 오브젝트입니다.

* **4. 인스펙터 창 (Inspector Window)**
    * **특징:** 하이어라키 창이나 프로젝트 창에서 **선택한 오브젝트의 상세 정보, 속성, 조립된 컴포넌트(Component)들을 보여주고 수정**할 수 있는 창입니다. 예를 들어, 오브젝트의 좌표나 색상을 바꿀 때 이곳을 이용합니다.

* **5. 프로젝트 창 (Project Window)**
    * **특징:** 게임 제작에 필요한 모든 소스 파일(C# 스크립트, 이미지, 사운드, 3D 모델 등)이 보관되는 ‘에셋(Asset) 창고’입니다. 컴퓨터의 파일 탐색기(폴더)와 같은 역할을 합니다.

* **6. 콘솔 창 (Console Window)**
    * **특징:** 프로그램 실행 중 발생하는 **로그(Log), 경고(Warning), 에러(Error) 메시지를 출력**해 주는 창입니다. 스크립트 코드의 오류를 찾아내거나(디버깅), 내가 원하는 값이 잘 나오는지 확인할 때 반드시 확인해야 하는 창입니다.

