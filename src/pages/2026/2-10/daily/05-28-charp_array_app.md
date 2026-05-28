---
layout: ../../../../layouts/PostLayout.astro
title: "05-28(목) 6.C# 배열의 활용"
date: "2026-05-28"
---

## 배열의 활용

### 직선 만들기

숫자 n을 입력 받아서 n번 반복되는 * 로 채워진 직선을 만든다.

```csharp
using System;
namespace Sungil
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            // N 입력받으면 길이 N 의 직선출력한다. (for문 이용)
            for(int i=0; i<n; i++) Console.Write("*");
            
        }
    }
}
```

실행 결과

```text
> 10
**********
```

### 정사각형 만들기

숫자 n을 입력 받아서 * 로 채워진 가로 n, 세로 n 의 정사각형을 만든다.

```csharp
using System;
namespace Sungil
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            // 2중 반복문을 이용한 사각형 그리기
            for(int i=0; i<n; i++) {
              for(int j=0; j<n; j++) {
                Console.Write("*");
              }
              Console.WriteLine();
            }
        }
    }
}
```

실행 결과

```text
> 5
*****
*****
*****
*****
*****
```

### 삼각형 만들기

숫자 n을 입력 받아서 * 로 채워진 가로 n, 세로 n 의 삼각형을 만든다.

```csharp
using System;
namespace Sungil
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            // 2중 반복문을 이용한 삼각형 그리기
            for(int i=1; i<=n; i++) {
              for(int j=0; j<i; j++) {
                Console.Write("*");
              }
              Console.WriteLine();
            }
        }
    }
}
```

실행 결과

```text
> 10
*
**
***
****
*****
******
*******
********
*********
**********
```