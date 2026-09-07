---
layout: ../../../../layouts/PostLayout.astro
title: "1학기 수행평가 2 (실습형) 준비"
date: "2026-04-20"
---

## 1. 사용자 정보 입력과 출력

```csharp
using System;
namespace sungil
{
    class Program
    {
        static void Main(string[] args)
        {
            string myName = Console.ReadLine();
            Console.WriteLine($"환영합니다. {myName}님!");
        }
    }
}
```

**입력 예시**

```text
성일
```

**출력 예시**

```text
환영합니다. 성일님!
```

## 2. 게임 캐릭터 상태 확인 및 분기

```csharp
using System;
namespace sungil
{
    class Program
    {
        static void Main(string[] args)
        {
            int hp = 30;
            int level = 15;

            // 체력이 50 미만이거나(OR) 레벨이 10 이상인 경우를 판별합니다.
            bool isDanger = (hp < 50) || (level >= 10);

            // isDanger 변수가 참일 경우와 거짓일 경우를 분기합니다.
            if( isDanger )
            {
                Console.WriteLine("경고 상태입니다.");
            } else
            {
                Console.WriteLine("안전 상태입니다.");
            }
        }
    }
}
```

**출력 결과**

```text
경고 상태입니다.
```

## 3. 문자열 처리 및 복합 조건식 작성

```csharp
using System;
namespace sungil
{
    class Program
    {
        static void Main(string[] args)
        {

        string inventory = "낡은 검, 지도, 열쇠";

        // 인벤토리에 "열쇠"가 포함되어 있는지 확인합니다.
        bool hasKey = inventory.Contains("열쇠");

        // 무기를 업그레이드하기 위해 "낡은 검"을 "전설의 검"으로 교체합니다.
        inventory = inventory.Replace("낡은", "전설의");

        int playerLevel = 25;
        // 플레이어의 레벨이 20 이상이고 (AND), 열쇠를 가지고 있는지(hasKey 변수가 true)를 
        // 동시에 판별하는 복합 조건식을 완성하세요.
        bool canEnter = (playerLevel >= 20) && (hasKey);
        Console.WriteLine($"canEnter = {canEnter}");
        }
    }
}
```

**출력 결과**

```text
canEnter = True
```