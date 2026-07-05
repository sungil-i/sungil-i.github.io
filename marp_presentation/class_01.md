---
marp: true
theme: default
paginate: true
backgroundColor: #f8f9fa
---

# 🧑‍🏫 Java 조건문 실습
성일정보고등학교 박원준 선생님

---

## 1. if문의 이해
조건이 **참(true)**일 때만 블록 안의 코드가 실행됩니다.

* (클릭 시 나타남) 조건식에는 비교 연산자가 들어갑니다.
* (클릭 시 나타남) 중괄호 `{ }` 로 실행할 구역을 묶어줍니다.

---

## 2. 실습 코드 작성
아래 코드를 따라 쳐봅시다.

```java
int score = 85;

if (score >= 80) {
    System.out.println("합격입니다!");
}