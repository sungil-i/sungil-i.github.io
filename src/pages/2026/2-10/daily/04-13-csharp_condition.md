---
layout: ../../../../layouts/PostLayout.astro
title: "04-13(월) 3.C# 조건문"
date: "2026-04-13"
---

<!-- 
```csharp

```
-->

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
int score = 55;
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

- 논리 연산자( AND &&, OR ||, NOT ! )

**AND 연산자**

| A | B | **A && B** |
| :-: | :-: | :-: |
| 참(true) | 참(true) | **참(true)** |
| 참(true) | 거짓(false) | **거짓(false)** |
| 거짓(false) |참(true) | **거짓(false)** |
| 거짓(false)| 거짓(false) | **거짓(false)** |



**OR 연산자**

| A | B | **A \|\| B** |
| :-: | :-: | :-: |
| 참(true) | 참(true) | **참(true)** |
| 참(true) | 거짓(false) | **참(true)** |
| 거짓(false) | 참(true) | **참(true)** |
| 거짓(false) | 거짓(false) | **거짓(false)** |

**예시1**

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