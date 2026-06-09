---
layout: ../../../../layouts/PostLayout.astro
title: "수행평가 3 (실습형) 준비"
date: "2026-06-04"
---

## 유니티 수행평가 3 예상문제

1. 유니티 '2D Universal' 프로젝트를 생성하고, 씬(Scene) 이름을 변경한다.
    * 프로젝트 이름: `my_unity`
        * 화면구성: `16:9 Aspect`
    * 씬 이름: `SampleScene` → `MainScene`
    * 완성된 프로젝트를 제출용 파일로 만들기: 메뉴에서 `Assets` > `Export As Asset Package` 로 내 프로젝트 파일을 추출한다. (`학번-이름.unitypackage`)

![수행3](../../../../assets/images/2026-application-test-3(20).jpg)

2. Player 만들기
    * 사각형 모양, 원 모양의 Sprite 만들기
        * 사각형 모양: `Player` (tag: `Player`)
        * 원 모양: `Goal` (tag: `Finish`)
    * 위치, 색깔 지정: 
        * 사각형 모양: `위치: X=-7, Y=-3, Z=0`, `색깔=노랑색`
        * 원 모양: `위치: X=7, Y=3, Z=0`, `색깔=빨강색`
    * 컴포넌트 추가:
        * 사각형 모양: `Rigidbody 2D`, `Box Collider 2D`
            * `Rigidbody 2D`: `Mass=1`, `Linear Damping=2`, `Angular Damping=2`, `Gravity Scale=0`
        * 원 모양: `Circle Collider 2D`
3. 키보드 조작하기
    * `Script Machine` 컴포넌트 추가: `PlayerMove.asset` 파일 생성
    * 키보드 입력 허용하기
        * 왼쪽 상단의 'Edit' 메뉴에서 'Project Settings' 를 선택한다.
        * 왼쪽의 'Player' 탭을 선택하고, 'Other Settings' 의 'Active Input Handling' 을 선택한다.
        * 'Active Input Handling' 에서 'Both' 를 선택한다.
    * 좌, 우, 상, 하 키보드 움직임 추가하기
        * `On Keyboard Input` 노드, `Rigidbody 2D: Set Linear Velocity` 노드 추가

## 유니티 수행평가 3 학습자료

### 1. 유니티 프로젝트 생성하기

1. 'Universal 2D' 선택하기
2. 프로젝트 이름: 'Miro-Game'
3. 위치: 'C:\Users\User\Desktop\Unity Workspace'

![수행3](../../../../assets/images/2026-application-test-3(1).png)

### 2. Scene 

**Scene 이름 바꾸기**

1. 왼쪽 하단의 'Project' 메뉴에 가서 'Assets' 에서 'Scenes' 를 선택한다.
2. 'SampleScene' 을 'MainScene' 으로 이름을 바꾼다.

![수행3](../../../../assets/images/2026-application-test-3(2).png)

**게임 화면 조정하기**

1. 가운데 '미리보기' 화면에서 화면 비율을 '16:9 Aspect' 로 바꾼다.

![수행3](../../../../assets/images/2026-application-test-3(9).png)

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

![수행3](../../../../assets/images/2026-application-test-3(3).png)

#### Component 추가하기

##### Rigidbody 2D

1. 'Add Component' 를 누르고 'Rigidbody 2D' 를 추가한다.
2. 속성을 Mass=1, Linear Damping=2, Angular Damping=2, Gravity Scale=0 으로 설정한다.

![수행3](../../../../assets/images/2026-application-test-3(4).png)

##### Box Collider 2D

1. 'Add Component' 를 누르고 'Box Collider 2D' 를 추가한다.

![수행3](../../../../assets/images/2026-application-test-3(5).png)

##### 키보드로 Player 조작하기

**키보드 입력 추가하기**

1. 왼쪽 상단의 'Edit' 메뉴에서 'Project Settings' 를 선택한다.
2. 왼쪽의 'Player' 탭을 선택하고, 'Other Settings' 의 'Active Input Handling' 을 선택한다.
3. 'Active Input Handling' 에서 'Both' 를 선택한다.

![수행3](../../../../assets/images/2026-application-test-3(6).png)

**Script Machine 추가하기**

1. 'Player' Object 에서 'Add Component'을 선택하고 'Script Machine' 을 추가한다.
2. 'Graph' 항목에서 'New' 를 선택한 뒤에 'PlayerControl' 이름의 Asset 파일을 추가한다.

![수행3](../../../../assets/images/2026-application-test-3(7).png)

![수행3](../../../../assets/images/2026-application-test-3(8).png)

**키보드로 조작하기**

**'On Keyboard Input' 노드 추가하기**

1. 'Script Machine'의 'Edit Graph' 를 클릭한다.
2. 빈공간에서 마우스 오른쪽 클릭을 해서 'On Keyboard Input' 노드를 추가한다.
3. 'On Keyboard Input' 노드의 Key=Right Arrow, Action=Hold 로 바꾼다.

![수행3](../../../../assets/images/2026-application-test-3(10).png)

**'RigidBody 2D: Set Linear Velocity' 노드 추가하기**

1. 빈공간에서 마우스 오른쪽 클릭을 해서 'RigidBody 2D: Set Linear Velocity' 노드를 추가한다.
2. 'RigidBody 2D: Set Linear Velocity' 노드의 2개의 입력칸 중 1번째 입력칸이 X 방향이다.
3. 'RigidBody 2D: Set Linear Velocity' 노드의 1번째 입력칸에 2를 입력한다. (X방향으로 속도를 2 증가시킨다는 말이다.)
4. 'On Keyboard Input' 노드의 오른쪽 삼각형을 'RigidBody 2D: Set Linear Velocity' 노드의 왼쪽 삼각형을 연결시킨다. (삼각형은 흐름을 나타낸다. 즉, 'On Keyboard Input' 노드 다음에 'RigidBody 2D: Set Linear Velocity' 노드를 실행시키라는 말이다.)

![수행3](../../../../assets/images/2026-application-test-3(11).png)

![수행3](../../../../assets/images/2026-application-test-3(12).png)

**키보드 방향키에 연결하기**

1. 노드를 선택해서 'Duplicate Selection' 으로 3개 더 복제한다. 
2. 각 키보드의 키를 'Left Arrow', 'Up Arrow', 'Down Arrow' 연결한다. 
3. 각 키보드에 따른 속도의 방향을 아래와 같이 바꿔준다. 

* 'Right Arrow': 첫번째빈칸=2, 두번째빈칸=0
* 'Left Arrow': 첫번째빈칸=-2, 두번째빈칸=0
* 'Up Arrow': 첫번째빈칸=0, 두번째빈칸=2
* 'Down Arrow': 첫번째빈칸=0, 두번째빈칸=-2

![수행3](../../../../assets/images/2026-application-test-3(13).png)

### 3. Goal 만들고 게임오버 화면 연결하기

**Goal 만들기**

1. 'Hierachy' 에서 '2D Object' > 'Sprites' > 'Circle' 을 추가한다.
2. 이름을 'Goal' 로 바꾸고 색깔을 빨간색(Red)으로 바꾼다.
3. 오른쪽 'Inspector' 에서 'Tag' 를 'Finish' 로 선택한다.

![수행3](../../../../assets/images/2026-application-test-3(16).png)

**게임오버 Scene 추가하기**

1. 왼쪽 하단의 'Project' > 'Assets' > 'Scenes' 화면의 빈 공간에서 마우스 우클릭을 한다.
2. 'Create' > 'Scene' > 'Scene' 으로 새로운 화면을 만든다.
3. 이름을 'FinishScene' 으로 바꾼다.

![수행3](../../../../assets/images/2026-application-test-3(14).png)

**Build Profile 에 등록하기**

1. 먼저 'FinishScene'을 더블클릭해서 미리보기 화면에 연다.
2. 왼쪽 상단 'File' > 'Build Profiles' 를 선택한다.
3. 'Scene List' 탭을 열어서 'Add Open Scenes' 를 클릭해서 'FinishScene' 을 추가합니다.

![수행3](../../../../assets/images/2026-application-test-3(15).png)

**Player 가 닿는 기능 구현**

1. 'Goal' 에 'Add Component' 를 클릭하고 'Circle Collider 2D' 를 추가한다.
2. 'Circle Collider 2D' 에서 'Is Trigger' 를 체크한다.

![수행3](../../../../assets/images/2026-application-test-3(17).png)

3. 'Player' 의 'Script Machine' 을 열고 'On Trigger Enter 2D' 이벤트 노드를 추가한다.
4. 'Game Object: Compare Tag' 노드, 'If' 노드, 'Scene Manager: Load Scene by Scene Name' 노드를 추가한다.
5. 만약 Player 와 부딪힌 Object의 Tag 가 'Finish' 라면 'FinishScene' 을 불러서 Scene 을 이동하는 기능을 구현한다.

![수행3](../../../../assets/images/2026-application-test-3(18).png)