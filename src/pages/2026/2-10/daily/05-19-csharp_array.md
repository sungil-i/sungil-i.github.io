---
layout: ../../../../layouts/PostLayout.astro
title: "05-19(화) 6.C# 배열"
date: "2026-05-19"
---

## 배열

> 배열은 같은 자료형이 연속적으로 저장된 형태입니다.

**정수형 배열**

```csharp
int[] numbers = {1, 2, 3, 4, 5};
```

### 1-(1).문자열 배열

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

### 1-(4). 


### 1-(5). 배열을 꺼꾸로 출력하기

for문을 사용해서 배열을 꺼꾸로 출력할 수 있습니다.

```csharp
int[] numbers = {2, 4, 6, 8, 10, 12};
for(int i=5; i>=0; i--) {
    Console.WriteLine(i);
}
for(int i=numbers.Length-1; i>=0; i--) {
    Console.WriteLine($"{i}인덱스의 값={numbers[i]}");
}
```

실행 결과

```text
5
4
3
2
1
0
5인덱스의 값=12
4인덱스의 값=10
3인덱스의 값=8
2인덱스의 값=6
1인덱스의 값=4
0인덱스의 값=2
```