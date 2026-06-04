---
layout: ../../../../layouts/PostLayout.astro
title: "수행평가 3 (실습형) 준비"
date: "2026-06-04"
---

## 유니티 수행평가 3

### 1. 유니티 프로젝트 생성하기

1. 'Universal 2D' 선택하기
2. 프로젝트 이름: 'Miro-Game'
3. 위치: 'C:\Users\User\Desktop\Unity Workspace'

![수행1-1](../../../../assets/images/2026-application-test-3(1).png)

### 2. Scene 이름 바꾸기

1. 왼쪽 하단의 'Project' 메뉴에 가서 'Assets' 에서 'Scenes' 를 선택한다.
2. 'SampleScene' 을 'MainScene' 으로 이름을 바꾼다.

![수행1-1](../../../../assets/images/2026-application-test-3(2).png)

### 2. Player 만들기

#### Object 생성하기

1. 오른쪽 상단의 'Hierarchy' 메뉴에 가서 빈공간에 마우스 우클릭을 한다.
2. '2D Object' > 'Sprites' > 'Square' 를 선택해서 Object 를 생성한다.
3. Object 이름을 'Player' 로 바꾼다.

#### Object 속성 바꾸기

1. 오른쪽 'Inspector' 메뉴에서 'Transform' 항목의 'Position' 을 선택한다.
2. 'Position' 의 X=-5, Y=-4 로 설정한다.
3. 'Sprite Renderer' 에서 'Color' 항목을 선택한다.
4. 색깔을 노란색(Yellow) 으로 바꾼다.

![수행1-1](../../../../assets/images/2026-application-test-3(3).png)

#### Component 추가하기

##### Rigidbody 2D

1. 'Add Component' 를 누르고 'Rigidbody 2D' 를 추가한다.
2. 속성을 Mass=1, Linear Damping=2, Angular Damping=2, Gravity Scale=0 으로 설정한다.

![수행1-1](../../../../assets/images/2026-application-test-3(4).png)

##### Box Collider 2D

1. 'Add Component' 를 누르고 'Box Collider 2D' 를 추가한다.

![수행1-1](../../../../assets/images/2026-application-test-3(5).png)