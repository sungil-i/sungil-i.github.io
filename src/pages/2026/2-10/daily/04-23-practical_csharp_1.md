---
layout: ../../../../layouts/PostLayout.astro
title: "04-23(목) 5.C# 응용 (1) 조건문+반복문"
date: "2026-04-20"
---

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