---
layout: ../../../../layouts/PostLayout.astro
title: "04-06(월) 1.시샵 첫 수업 (2)"
date: "2026-04-06"
---

<!-- 
```csharp

```
-->

## 시샵(C# 첫걸음)

> 4월 6일 월요일

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

첫번째 방법 (일반적인 방법 )

```csharp
Console.WriteLine("첫번째 줄");
Console.WriteLine("두번째 줄");
Console.WriteLine("세번째 줄");
```

두번째 방법 (특수 기호 넣기 \\n)

```csharp
Console.WriteLine("첫번째 줄\n두번째 줄\n세번째 줄");
```

세번째 방법 (문자열 리터럴 사용 @)

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

### 5.프로그램 멈춰 세우기

프로그램이 실행 직후 바로 꺼지는 것을 방지하는 필수 명령어입니다.

```csharp
Console.ReadKey();
```