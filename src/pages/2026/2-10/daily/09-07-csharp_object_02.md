---
layout: ../../../../layouts/PostLayout.astro
title: "09-07(월) 7. C# 객체지향 기초 (2): 클래스와 인스턴스"
date: "2026-09-07"
---

## Pet 객체 설계하기

> Codespaces(https://github.com/codespaces) 에서 VS Code 웹 버전으로 프로젝트를 엽니다.

### 객체 생성 (1)

![수행1-1](../../../../assets/images/2026-09-01-Pet_1.png)

게임 화면에 나타나는 변수명은 `mypet`이고, 객체의 이름은 "Skittles"인 클래스를 설계한다.

#### 클래스 설계

C# 소스코드

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

* **생성자 함수**: 클래스 이름과 같은 멤버함수를 만들어 놓으면,<br>인스턴스를 생성할 때(new) 이 함수가 자동으로 실행됩니다.

#### 인스턴스 생성

> 설계해 놓은 클래스를 게임 화면에 나타나게 한다.

C# 소스코드

```csharp
Pet mypet = new Pet();
mypet.Name = "Skittles";
mypet.WhoAreYou();
```

실행결과

```text
객체 생성!
나의 이름은 Skittles 입니다.
```

### 객체 생성 (2)

* 생성자의 이름을 똑같이 만들고<br>파라미터만 다르게 할 수 있습니다.
* 파라미터를 다르게 하면 생성자를 2개 이상 만들 수 있습니다.
* 파라미터는 함수에서 변수를 넘겨받을 수 있게 만드는 매개체입니다.

![수행1-1](../../../../assets/images/2026-09-01-Pet_2.png)

#### 클래스 설계

C# 소스코드

```csharp
using System;

namespace HelloWorld
{
    public class Pet
    {
        // 멤버 변수
        public string Name;
        // 멤버 함수
        public Pet() // 생성자 멤버 함수 1
        {
            Console.WriteLine("객체 생성!");
        }
        public void WhoAreYou()
        {
            Console.WriteLine($"나의 이름은 {Name} 입니다.");
        }
        public Pet(string name) // 생성자 멤버 함수 2
        {
            this.Name = name; // this는 자기 자신 클래스를 가리키는 지시문입니다
            Console.WriteLine("객체 생성!");
            Console.WriteLine($"나의 이름은 {Name} 입니다.");
        }
    }
}
```

#### 인스턴스 생성

C# 소스코드

```csharp
Pet kiwi = new Pet("Kiwi");
```

실행결과

```text
객체 생성!
나의 이름은 Kiwi 입니다.
```

### 오버로드(Overload)

멤버 함수를 만들 때, 파라미터를 다르게 만들어서<br>파라미터별로 서로다른 멤버 함수를 호출할 수 있도록 설계하는 방식

C# 소스코드

```csharp
using System;

namespace HelloWorld
{
    public class Pet
    {
        // 멤버 변수
        public string Name;
        // 멤버 함수
        public Pet() // 생성자 1
        {
            Console.WriteLine("객체 생성!");
        }
        public Pet(string name) // 생성자 2 (오버로드)
        {
            this.Name = name;
            Console.WriteLine("객체 생성!");
            Console.WriteLine($"나의 이름은 {Name} 입니다.");
        }
        public Pet(string name, int hp) // 생성자 3 (오버로드)
        {
            this.Name = name;
            Console.WriteLine("객체 생성!");
            Console.WriteLine($"나의 이름은 {Name} 입니다.");
        }
        public Pet(string name, int hp, double speed) // 생성자 4 (오버로드)
        {
            this.Name = name;
            Console.WriteLine("객체 생성!");
            Console.WriteLine($"나의 이름은 {Name} 입니다.");
        }
    }
}
```












