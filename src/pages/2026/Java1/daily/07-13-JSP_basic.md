---
layout: ../../../../layouts/PostLayout.astro
title: "3. JSP 기초"
date: "2026-07-13"
---

## JSP 란 무엇인가?

JSP = Java Server Page

**HTML vs. JSP**

* HTML: 정적인 웹 페이지 
* JSP: 동적인 웹 페이지 (정보를 주고 받고 할 수 있다.)

**서버와 클라이언트**

* 서버: 데이터를 제공하는 컴퓨터 (JSP)
* 클라이언트: 데이터를 제공 받는 컴퓨터 (HTML)

**JSP 작성하기**

정적 HTML은 100번을 새로고침해도 항상 똑같은 글자만 보여줍니다. 반면 **JSP(JavaServer Pages)**는 HTML 문서 한가운데에 자바 코드 엔진을 장착한 파일입니다. 

* `<% 자바 코드 %>` (스크립트릿): 이 안에서는 콘솔에서 쓰던 순수 자바 문법을 그대로 쓸 수 있습니다. (화면에는 안 보임)
* `<%= 자바 변수 %>` (표현식): 자바 변수에 담긴 진짜 값을 HTML 글자로 바꿔서 화면에 띄워줍니다.

JSP 예제 1

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>나의 첫 JSP</title>
</head>
<body>
    <h1>안녕하세요! 첫 자바 웹페이지입니다.</h1>
    
    <%
        // 이 블록 안은 순수한 자바(Java) 컴퓨터 세상입니다!
        String schoolName = "성일정보고";
        int studentId = 20301;
        String studentName = "홍길동";
    %>

    <hr>
    <h3>학교: <%= schoolName %></h3>
    <p>학번: <strong><%= studentId %></strong></p>
    <p>이름: <strong><%= studentName %></strong></p>
</body>
</html>
```

JSP 예제 2

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>나의 첫 JSP</title>
</head>
<body>
    <h2>👋 환영합니다! 동적 웹의 세계로!</h2>
    
    <%
        // [Java 블록] 변수 선언 및 데이터 저장 (브라우저에는 이 코드가 보이지 않습니다)
        String myName = "홍길동";
        int myAge = 16;
        int nextYearAge = myAge + 1;
    %>

    <hr>
    <ul>
        <li>이름: <strong><%= myName %></strong></li>
        <li>올해 나이: <strong><%= myAge %></strong> 세</li>
        <li>내년 나이: <strong><%= nextYearAge %></strong> 세</li>
    </ul>
</body>
</html>
```


## Form 태그로 자료 주고 받기

* request: 클라이언트가 서버에게 자료를 요청
* response: 서버가 클라이언트에게 자료를 제공

![자료주고받기](../../../../assets/images/request-response.png)

## JSP 에서 서버로 자료를 보내는 방법

* GET 방식(엽서): 주소창 URL 뒤에 우리가 보낸 데이터가 `?dan=5` 처럼 그대로 노출됩니다. 누구나 볼 수 있지만, 데이터가 어떻게 넘어가는지 우리 눈으로 직접 확인할 수 있어 오늘 실습에 아주 적합합니다.

* POST 방식(편지봉투): 주소창에 보이지 않게 데이터를 봉투 안에 꽁꽁 숨겨서 보냅니다. 로그인할 때 아이디나 비밀번호처럼 남이 보면 안 되는 중요한 정보를 보낼 때 사용합니다.

JSP + Form 예제 1

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>구구단 만들기</title>
</head>

<body>
    <div>
        <a href="./">HOME</a>&nbsp;&nbsp;
        <a href="ex1.jsp">예제1</a>&nbsp;&nbsp;
        <a href="ex2.jsp">예제2</a>&nbsp;&nbsp;
        <a href="ex3.jsp">예제3</a>&nbsp;&nbsp;
        <a href="ex4.jsp">예제4</a>&nbsp;&nbsp;
        <a href="ex5.jsp">예제5</a>&nbsp;&nbsp;
    </div>
<h1>구구단 결과</h1>

<p>원하시는 구구단의 '단'을 선택하고 출력 버튼을 눌러주세요</p>

<form method="get">
    <select name="dan">
        <option value="2">2단</option>
        <option value="3">3단</option>
        <option value="4">4단</option>
        <option value="5">5단</option>
        <option value="6">6단</option>
        <option value="7">7단</option>
        <option value="8">8단</option>
        <option value="9">9단</option>
    </select>
    <button type="submit">출력</button>
</form>

<br>
    <%
    String danText = request.getParameter("dan");
    if(danText != null) {
        int dan = Integer.parseInt(danText);
    %>
    <ul>
        <%
        for( int i = 1; i<=9; i++) {
        %>
        <li><%=dan%> x <%=i%> = <%=(dan*i)%></li>
        <%
        }
        %>
    </ul>
    <%
    }
    %>
</body>
</html>
```

JSP + Form 예제 2

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>배경색 바꾸기</title>
</head>
<% String bgText=request.getParameter("bg");
if(bgText !=null) { %>
<body style="background-color: <%=bgText%>;">
<% } else { %>
<body>
<% } %>
    <div>
        <a href="./">HOME</a>&nbsp;&nbsp;
        <a href="ex1.jsp">예제1</a>&nbsp;&nbsp;
        <a href="ex2.jsp">예제2</a>&nbsp;&nbsp;
        <a href="ex3.jsp">예제3</a>&nbsp;&nbsp;
        <a href="ex4.jsp">예제4</a>&nbsp;&nbsp;
        <a href="ex5.jsp">예제5</a>&nbsp;&nbsp;
    </div>
    <h1>배경색 바꾸기</h1>

    <p>원하는 배경색을 선택하고 변경 버튼을 눌러주세요</p>

    <form method="get">
        <select name="bg">
            <option value="white">흰색</option>
            <option value="red">빨강색</option>
            <option value="blue">파랑색</option>
            <option value="yellow">노랑색</option>
        </select>
        <button type="submit">변경</button>
    </form>
</body>
</html>
```
