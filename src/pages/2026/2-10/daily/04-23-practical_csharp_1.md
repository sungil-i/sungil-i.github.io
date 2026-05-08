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
for(int i=1; i<100; i++) {
    string str = i.ToString();
    if(str.Contains("3")) Console.WriteLine("짝");
    else Console.WriteLine(str);
}
```

실행결과

```text
1
2
짝
4
5
6
7
8
9
10
11
12
짝
14
15
16
17
18
19
20
21
22
짝
24
25
26
27
28
29
짝
짝
짝
짝
짝
짝
짝
짝
짝
짝
40
41
42
짝
44
45
46
47
48
49
50
51
52
짝
54
55
56
57
58
59
60
61
62
짝
64
65
66
67
68
69
70
71
72
짝
74
75
76
77
78
79
80
81
82
짝
84
85
86
87
88
89
90
91
92
짝
94
95
96
97
98
99
```