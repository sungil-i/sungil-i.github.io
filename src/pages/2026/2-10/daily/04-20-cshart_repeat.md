---
layout: ../../../../layouts/PostLayout.astro
title: "04-20(월) 4.C# 반복문"
date: "2026-04-20"
---

## 4. 반복문

> 반복문과 친해지기 (for, while)

**게임이 돌아가는 원리**

이미지를 초당 x번씩 화면에 보여줍니다.<br>
code: 반복문(while)을 사용해서 서로 다른 이미지를<br>
일정 간격으로 화면에 뿌려준다.

- Start: 처음 화면
- Update: 움직이는 화면

### (1)-1. 1부터 5까지 숫자 세기 (for문)

**문법**

```csharp
// 시작값 ~ 끝나는 조건까지, 단계에 따라
// 코드를 반복해서 실행한다.
for( 시작값; 끝나는 조건; 단계 ) {
    코드;
}
```

예시

> for문을 사용하여 1부터 5까지 숫자를 순서대로 출력하기

```csharp
for(int i=1; i<=5; i=i+1) {
    Console.WriteLine($"{i}번째 반복");
}
```

실행결과

```text
1번째 반복
2번째 반복
3번째 반복
4번째 반복
5번째 반복
```

### (1)-2. 카운트 다운 (while문)

**문법**

조건이 참(true)일 동안 코드를 반복합니다.<br>
while 문은 조건에 따라 무한 반복할 수 있습니다.

```csharp
while(조건) {
    코드;
}
```

예시

> while문을 사용하여 3부터 1까지 <br>숫자를 거꾸로 줄여가며 카운트다운을 합니다.

```csharp
int count = 3;
while(count > 0) {
    Console.WriteLine($"카운트 다운: {count}");
    count = count - 1;
}
```

실행결과

```text
카운트 다운: 3
카운트 다운: 2
카운트 다운: 1
```

### (1)-3. 짝수만 건너뛰기 (continue)

continue 를 만나면<br>아래 코드를 무시하고 **다음 반복**으로 넘어갑니다.

예시

> 1부터 5까지 반복하다가,<br>i가 3일 때는 continue를 사용해 건너뛰세요.

```csharp
for(int i=1; i<=5; i=i+1) {
    if(i == 3) {
        continue;
    }
    Console.WriteLine($"{i}번째 반복");
}
```