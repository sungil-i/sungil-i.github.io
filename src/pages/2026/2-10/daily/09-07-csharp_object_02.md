---
layout: ../../../../layouts/PostLayout.astro
title: "09-07(월) 7. C# 객체지향 기초 (2)"
date: "2026-09-07"
---

## Pet 객체 설계하기

> Codespaces(https://github.com/codespaces) 에서 VS Code 웹 버전으로 프로젝트를 엽니다.

### 객체 생성 (1)

![수행1-1](../../../../assets/images/2026-09-01-Pet_1.png)

게임 화면에 나타나는 변수명은 `mypet`이고, 객체의 이름은 "Skittles"인 클래스를 설계한다.

#### 클래스 설계

```csharp
using System;

namespace HelloWorld
{
    public class Pet
    {
        // 멤버 변수
        public string Name;
        // 멤버 함수
        public Pet() // 생성자
        {
            Console.WriteLine("객체 생성!");
        }
        public void WhoAreYou()
        {
            Console.WriteLine($"나의 이름은 {Name} 입니다.");
        }
    }
}
```

#### 인스턴스 생성

### 객체 생성 (2)



















