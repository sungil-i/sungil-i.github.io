---
layout: ../../../../layouts/PostLayout.astro
title: "04-13 3.C# 조건문"
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