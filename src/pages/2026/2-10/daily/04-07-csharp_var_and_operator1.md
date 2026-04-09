---
layout: ../../../../layouts/PostLayout.astro
title: "04-07 2.시샵 둘째 수업 (1)"
date: "2026-04-07"
---

<!-- 
```csharp

```
-->

## 2.변수와 연산자

### (1)-1. 정수형 변수 활용하기

- 플레이어의 레벨(int)을 15로 선언하세요.
- 게임 서버 전체 사용자의 총 경험치(long)를 9000억으로 선언하세요. (900000000000L)

```csharp
int level = 15;
long totalExp = 9000000000000L;
Console.WriteLine($"레벨: {level}, 총 경험치: {totalExp}");
```

### (1)-2. 소수점 데이터 다루기

- 원주율(float)을 3.14로 선언하세요. (f 접미사 활용)
- 아주 정밀한 물리 상수(double)를 0.0000000123으로 선언하세요.

```csharp
float pi = 3.14f;
double physic = 0.00000000123;
Console.Write($"파이: {pi}, 더블변수: {physic}");
```

### (1)-3. 텍스트 데이터 선언하기

- 아이템 등급(char)을 'S'로 선언하세요.
- 아이템 이름(string)을 "전설의 검"으로 선언하세요.

> **char 은 문자 1개: 작은따옴표(')**

> **string 은 문자열: 큰따옴표(")**

```csharp
char itemGrade = 'S';
string itemName = "전설의 검";
Console.WriteLine($"[{itemGrade}] {itemName}");
```

### (1)-4. 논리형 데이터

> 논리형 데이터: 참/거짓 판별할 때 쓰이는 변수

- 퀘스트 완료 여부(bool: 불)를 true로 선언하세요.
- 로그인 중인지 여부(bool: 불)를 false로 선언하세요.

(비교) 자바: boolean 불린 

```csharp
bool isQuestComplete = true;
bool isLogin = false;
Console.WriteLine($"퀘스트 완료: {isQuestComplete}");
Console.WriteLine($"로그인 중: {isLogin}");
```

### (1)-5. 변수 값 업데이트

> 기존 변수를 선언한 뒤 새로운 값을 할당할 수 있습니다.

- int gold = 1000;
- gold 변수의 값을 1500으로 변경하고 출력하세요.

```csharp
int gold = 1000;
// 아이템 획득.. 코인 획득.. (+500)
gold = 1500;
Console.WriteLine($"현재 골드: {gold}");
```

### (2)-1. 산술 연산자

- int maxHp = 100;
- int damage = 35;
- maxHp에서 damage를 뺀 결과를 currentHp(int)에 저장하세요.
- currentHp를 출력하세요.

| 종류 | 연산자 |
|:-:| :-: |
| 더하기 | + |
| 빼기 |- |
| 곱하기 | * |
| 나누기 | / |
| 나머지 | % |
| 증가 연산자 | ++ |
| 감소 연산자 | -- |

```csharp
int maxHp = 100;
int damage = 35;
int currentHp = maxHp - damage;
currentHp = currentHp + 10;
Console.WriteLine($"현재 체력: {currentHp}");
```

### (2)-2. 비교, 논리 연산자

- 비교 연산자( >, <, >=, <=, == )
- 논리 연산자( AND &&, OR ||, NOT ! )

**AND 연산자**

| A | B | **A && B** |
| :-: | :-: | :-: |
| 참(true) | 참(true) | **참(true)** |
| 참(true) | 거짓(false) | **거짓(false)** |
| 거짓(false) |참(true) | **거짓(false)** |
| 거짓(false)| 거짓(false) | **거짓(false)** |

**AND 연산자 사용 예시**

> 레벨이 20 이상이고( && )<br>티켓을 가지고 있는지 여부를<br>canEnter(bool)에 저장하세요. <br>
> 그리고 canEnter를 출력하세요.

```csharp
int level = 25;
bool hasTicket = true;
bool canEnter = (level >= 25) && (hasTicket == true);
Console.WriteLine($"입장 가능 여부: {canEnter}");
```

**OR 연산자**

| A | B | **A \|\| B** |
| :-: | :-: | :-: |
| 참(true) | 참(true) | **참(true)** |
| 참(true) | 거짓(false) | **참(true)** |
| 거짓(false) | 참(true) | **참(true)** |
| 거짓(false) | 거짓(false) | **거짓(false)** |

**OR 연산자 사용 예시**

> 레벨이 20 이상거나( || )<br>티켓을 가지고 거나 할 때 입장 가능하다.<br>canEnter(bool)에 저장하세요. <br>
> 그리고 canEnter를 출력하세요.

```csharp
int level = 25;
bool hasTicket = true;
bool canEnter = (level >= 25) || (hasTicket == true);
Console.WriteLine($"입장 가능 여부: {canEnter}");
```