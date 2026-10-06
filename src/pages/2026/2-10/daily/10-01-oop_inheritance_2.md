---
layout: ../../../../layouts/PostLayout.astro
title: "10-01(목) 7. C# 객체지향 기초 (3): 상속 ②"
date: "2026-10-01"
---

<!--
![](../../../../assets/images/)
-->

## 객체지향 상속 (이론)

![](../../../../assets/images/2026-09-08-oop_inheritance_2.png)

![](../../../../assets/images/2026-09-08-oop_inheritance_1.png)

로블록스 Adopt me

### 객체지향 상속 (Override) 개념

**상속**: 부모 클래스의 멤버 변수와 멤버 함수를 자식 클래스에 물려주는 것

부모에게 물려받은 멤버 함수를 자녀 클래스에서 수정할 수 있다.

* `virtual`: 부모 클래스에서 수정 허용 권한을 주는 키워드이다.
* `override`: 자녀 클래스에서 부모 클래스의 멤버 함수를 수정하겠다는 표시를 하는 키워드이다.

## 객체지향 상속 (실습)

### 전체 클래스 설계

`Pet` 부모 클래스를 만들고, 이 클래스를 상속 받는 2개의 클래스를 만듭니다.

`Dog` 클래스와 `Frog` 클래스는 `Pet` 클래스를 부모로 갖는 자식 클래스입니다.

![](../../../../assets/images/2026-09-08-oop_inheritance_graph_2.png)

부모 클래스의 `move()` 함수와 `sound()` 함수가 있지만,

이것을 자식 클래스에서 그대로 사용하지 않고, 

수정해서 자신만의 기능을 구현해서 사용할 수 있다.

### `Pet` 클래스 설계 (부모 클래스)

`Pet` 클래스 C# 소스코드

```csharp
using System;

namespace HelloWorld
{
    public class Pet
    {
        // 멤버 변수
        public string Name;
        // 멤버 함수
        // virtual 키워드는 부모 클래스에서 자식 클래스에게 수정 권한을 부여하는 것이다.
        public virtual void move() 
        {
            Console.WriteLine("움직인다..");
        }
        public virtual void sound()
        {
            Console.WriteLine("소리를 낸다!");
        }
    }
}
```

### `Dog` 클래스 설계 (자식 클래스 1)

### `Frog` 클래스 설계 (자식 클래스 2)










































