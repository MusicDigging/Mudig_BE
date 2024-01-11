# Mudig

![phone34-min](https://github.com/MusicDigging/Mudig_BE/assets/107661525/6fc4b1ca-6ca0-4f59-8acb-e3c15ff79127)
![-2__1_6](https://github.com/MusicDigging/Mudig_BE/assets/107661525/2e99de8b-744c-4d44-8123-6e151f422698)
![-2__1](https://github.com/MusicDigging/Mudig_BE/assets/107661525/27c4a96e-313e-4f10-9956-294f9cf556e5)

[뮤딕 바로가기](https://www.mudig.co.kr/)

```
해당 서비스를 이용해보실 수 있는 테스트 계정입니다.

 ID : mudig011@email.com
 PW : Mudig011

 ID : mudig012@email.com
 PW : Mudig012

 ID : mudig013@email.com
 PW : Mudig013

 ID : mudig014@gmail.com
 PW : Mudig014

 ID : mudig015@gmail.com
 PW : Mudig015
```

## **[목차]**

1. [개요](#계기-및-목표)
2. [기능](#1-목표와-기능)<br>
   a. [주요 기능](#11-주요-기능)
3. [개발 환경 및 배포 URL](#2-개발-환경-및-배포-URL)<br>
   a. [개발 환경](#21-개발-환경)<br>
   b. [배포 환경](#22-배포-환경)
4. [프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)<br>
   a. [ERD](#31-entity-relationship-diagram)<br>
   b. [요구사항 정의서](#32-요구사항-정의서)<br>
   c. [API 명세서](#33-api-명세서)<br>
   d. [URL 설계](#34-url-설계)<br>
   e. [Architecture](#35-프로젝트-설계-및-프로세스)<br>
   f. [개발 일정](#36-개발-일정)<br>
   g. [git 전략](#37-git-branch-전략)
5. [구현 기능 시연](#4-기능)
6. [개발하며 느낀점](#5-개발하며-느낀점)<br>
   a. [Open API Specification](#511-open-api-specification)<br>
   b. [CI/CD](#512-cicd)<br>
   c. [Restful API](#513-restfull-api)<br>
   d. [Oauth](#514-oauth)
7. [외부 어플리케이션](#6-외부-어플리케이션)<br>
   a. [ChatGPT](#chatgpt)<br>
   b. [Karlo](#karlo)<br>
   c. [Youtube Data API](#youtube-data-api)<br>
8. [유저 피드백 후 반영](#7-유저-피드백-후-반영)

## 계기 및 목표

### 1️⃣ AI는 아직 사람들과 친해지지 않았다.

### 2️⃣ AI에 대한 부정적인 시선을 낮추고, 사람들과 친해지는 계기를 제공하자!

```
현재 AI 기술은 사람들에게 많은 관심을 받고 있지만
아직도 많은 사람들과는 친해지지 않았습니다.

그래서 우리의 서비스를 통해 좀더 친해질 수 있는 기회를 제공하고 싶었습니다.
```

## 인사말

안녕하세요. 🙇‍♂️

뮤딕(Mudig, Music Digging 이하 뮤딕)은 사용자들이 새로운 음악을 발견하고, 추천받으며, 공유할 수 있는 플랫폼을 말합니다.

GPT (Generative Pretrained Transformer) 기술과 Karlo(T2I, Text to Image)를 사용하여 개인화된 음악 추천과 인터렉티브한 경험을 제공하는 서비스입니다.

뮤딕은

1.  자체 회원가입 뿐만 아니라 구글, 카카오를 이용한 소셜 로그인을 지원하고 있습니다.
2.  인공지능을 통해 새로운 음악을 찾는 즐거움을 드릴 수 있습니다.
3.  자신만의 플레이리스트를 공유하고, 소통하며 무료한 일상에 소소함 즐거움을 느낄 수 있도록 장소를 제공해드립니다.

### 디깅이란?

```
‘디깅’이란 원래 디제이가 자신의 공연 리스트를 채우기 위해서
음악을 찾는 행위를 의미하나, 현재는 자신의 특색있는 플레이리스트를 짜는 것으로
그 의미가 확대 되어 일반인들도 사용하는 언어가 되었습니다.
```

## 팀원 소개

### 안녕하세요. Team Mudig 입니다!

| 강현우                                                | 김여주                                                | 사수봉                                            | 심민정                                            | 황봉수                                            |
| ----------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| <a href="https://github.com/Hyunwooz">🔗 Hyunwooz</a> | <a href="https://github.com/kimyeoju">🔗 kimyeoju</a> | <a href="https://github.com/su0797">🔗 su0797</a> | <a href="https://github.com/MJ-SIM">🔗 MJ-SIM</a> | <a href="https://github.com/bnbbbb">🔗 bnbbbb</a> |

안녕하세요 🙇‍♂️<br>
저희는 Mudig의 주니어 개발자 백엔드 팀 입니다.<br>
Estsoft에서 주관하는 백엔드 오르미 교육과정에서 만난 비전공자와 전공자들로 이루어져 있습니다. 새로운 기술을 받아들임에 있어서 열린 마음을 가진 분들이 모여 프로젝트를 진행하였습니다.<br>
기술적으로 부족할 수도 있지만 최선을 다해 준비했습니다.<br>
잘부탁드립니다 :)

### 역할

![백엔드 역할](https://github.com/MusicDigging/Mudig_BE/assets/107661525/a929aedb-2092-4eb6-9e56-8cd2ea4c6598)

### 협업 도구

📜 Notion , 📱 Discord

#### Discord Webhook을 통한 Gitgub 연동

해당 프로젝트를 Github으로 관리를 하면서 Commit Log를 협업 메신저로 사용하고 있는 Discord에서 알림을 받을 수 있도록 연동 하였습니다.

##### 1. Discord Webhook 생성

![스크린샷 2024-01-08 111902](https://github.com/MusicDigging/Mudig_BE/assets/107661525/cda488e2-912b-4617-8fa6-278bd233e264)

##### 2. Github Webhook 생성

![스크린샷 2024-01-08 112032](https://github.com/MusicDigging/Mudig_BE/assets/107661525/fd5cba69-8d97-404d-8207-550b295d7c12)

##### 3. Discord 알림 메시지 수신

![스크린샷 2024-01-08 111603](https://github.com/MusicDigging/Mudig_BE/assets/107661525/987b7b02-9ce0-4c64-a99b-5d036475c7c5)
![스크린샷 2024-01-08 111528](https://github.com/MusicDigging/Mudig_BE/assets/107661525/25407f46-39e6-405a-8490-bfa9eefe757c)
![스크린샷 2024-01-08 111544](https://github.com/MusicDigging/Mudig_BE/assets/107661525/1533b97a-5975-4223-b150-213687914f62)

## 1. 기능

### 1.1. 주요 기능

- 회원가입 및 로그인 , 소셜 로그인 (Kakao, Google)

  ```
  이메일을 통한 회원가입 뿐만 아니라 카카오, 구글을 이용한 소셜로그인 기능을 제공하고 있습니다.
  회원탈퇴와 비밀번호 변경 기능도 제공하고 있습니다.
  ```

- 이메일로 통한 회원가입시 메일 인증

  ```
  SMTP 서버를 통해 이메일 인증기능을 구현하였습니다.

  작성하신 이메일 주소로 인증번호가 발송됩니다.
  인증번호가 일치할 경우 회원가입이 가능합니다.
  ```

- JSON Web Token 인증 방식

  ```
  로그인시 발급된 Access Token을 통해서 유저 인증을 진행하는 기능을 제공하고 있습니다.
  ```

- 프로필 CRU

  ```
  회원가입 후 자신을 대표하는 프로필을 꾸밀 수 있는 기능을 제공하고 있습니다.
  프로필 이미지와 한줄 소개를 작성 뿐만아니라 관심 장르, 대표 플레이리스트 등을 설정 가능합니다.
  ```

- Follow / Unfollow 기능

  ```
  자신과 관심사가 비슷한 유저와 팔로워를 맺을 수 있습니다.
  ```

- 랜덤 뮤비

  ```
  우리 서비스에서 보유 중인 Music 목록에서 랜덤으로 5개의 음악을 추천해드리는 기능을 제공하고 있습니다.
  해당 기능을 통해 장르, 연도에 상관없이 다양한 음악을 랜덤으로 만나보실 수 있습니다.
  ```

- 플레이리스트 CRUD 기능

  ```
  사용자들이 원하는 내용을 토대로 플레이리스트 생성하는 기능을 제공하고 있습니다.
  수정에는 곡 순서 이동, 곡 삭제 기능이 있습니다.
  해당 기능은 GPT API, YouTube Data API, Karlo 와 연관되어 있습니다.
  ```

- 이벤트 플레이리스트 생성

  ```
  사용자들의 현재 상황,기분에 대한 플레이리스트를 생성할 수 있는 기능입니다.
  이 기능은 이벤트성으로 발생됩니다.
  ```

- 플레이리스트 좋아요

  ```
  뮤딕 이용 중 발견한 취향저격 플레이리스트에 좋아요를 눌러
  ‘마이페이지 - 좋아요 표시한 플레이리스트’에 저장할 수 있습니다.
  저장된 리스트는 내 프로필에 방문한 다른 유저들도 볼 수 있어
  서로 다양한 플레이리스트를 공유할 수 있습니다.
  ```

- 플레이리스트, 유저 검색 기능

  ```
  원하는 키워드를 입력 후 검색하면 플레이리스트의 제목, 유저의 닉네임
  또는 소개글에 해당 키워드가 포함된 플레이리스트와 유저를 찾아볼 수 있습니다.
  ```

- 댓글과 대댓글 CRUD

  ```
  댓글을 이용하여 게시글에 대한 의견을 남길 수도 있으며 댓글의 대댓글 기능 까지 지원하고 있습니다.
  댓글을 수정, 삭제하는 기능까지 제공 되고 있습니다.
  ```

- GPT API, YouTube Data API, Karlo

  ```
  사용자가 입력한 내용을 토대로 GPT API가 생성한 결과물을 YouTube Data API V3로
  전송하여 플레이리스트의 제목, 노래들, Karlo 이미지 값 등을 생성합니다.
  ```

  [# 외부 어플리케이션](#6-외부-어플리케이션)

## 2. 개발 환경 및 배포 URL

### 2.1. 개발 환경

Python == 3.11.3

Django == 4.2.7

AWS S3

- boto3 == 1.28.38

DRF

- djangorestframework == 3.14.0
- django-cors-headers == 4.3.1
- djangorestframework-simplejwt == 5.3.0

PostgreSQL

- psycopg2-binary == 2.9.9

Open Api Specification

- drf-spectacular == 0.26.5

KARLO (이미지 생성 AI)

- Karlo 2.0.4.0

ChatGPT (LLM, 문장 생성 AI)

- GPT Turbo 3.5

### 2.2. 배포 환경

#### 2.2.1. Back-End

Aws Ec2

- t2.micro

AWS S3

AWS RDS

- PostgreSQL 15.4-R3

### 2.3. 배포 URL

#### 2.3.1. Back-End

- https://api.mudig.co.kr/
- Back-End Repo : https://github.com/MusicDigging/Mudig_BE

#### 2.3.2. Front-End

- https://www.mudig.co.kr/
- Front-End Repo : https://github.com/MusicDigging/Mudig_FE

## 3. 프로젝트 구조와 개발 일정

### 3.1. Entity Relationship Diagram

![스크린샷 2024-01-02 203149](https://github.com/MusicDigging/Mudig_BE/assets/107661525/3162f5bb-6ca2-447a-978a-903dd4619c0a)

[DB-Diagram 바로가기](https://dbdiagram.io/d/AIP-6548a0187d8bbd64658ecdfe)

### 3.2. 요구사항 정의서

[요구사항 정의서 바로가기](https://docs.google.com/spreadsheets/d/1k1bcUxAqGr-WbKBvex_J7M51-aIQd9EQxcZN1uKBqaY/edit?pli=1#gid=0)

#### 프로젝트 범위

**뮤딕**은 ChatGPT를 기반으로 한 AI 음악 디깅 서비스입니다. 사용자들은 AI를 활용해 현재 기분이나 선호하는 음악 장르 등을 기반으로 플레이리스트를 생성할 수 있습니다. 또한, 생성한 플레이리스트를 공유하고 다른 사용자들과 댓글로 소통할 수 있습니다. 뮤딕은 소셜 음악 공유 플랫폼으로서 다양한 음악을 탐색하고 소통할 수 있는 공간으로, 음악을 즐기는 즐거운 경험을 제공합니다.

#### 용어집

| 용어          | 정의                                                                                                                                                                                                                                                                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 플레이리스트  | 플레이리스트는 음악이나 비디오, 사진, 텍스트 등을 모아 놓은 목록을 말합니다. 주로 음악 스트리밍 서비스에서는 한 테마나 분위기에 맞게 곡들을 모아둔 목록으로 이용되며. 일상의 배경음악부터 감성적인 분위기까지, 다양한 테마나 취향에 따라 플레이리스트를 만들어 공유하거나 즐길 수 있습니다. 종종 사용자들이 좋아하는 음악이나 선곡을 모아둔 목록으로도 사용됩니다. |
| 유저          | 유저(User)란 특정 웹사이트, 애플리케이션 또는 서비스를 이용하는 개인이나 기업을 가리킵니다. 이용자가 해당 플랫폼에 등록하고, 서비스를 이용하는 사람들을 의미합니다. "사용자" 또는 "고객"과 유사한 의미로 쓰입니다. 유저는 로그인하여 서비스에 접근하고, 서비스의 기능을 이용하며, 개인적인 프로필을 설정하고 정보를 관리할 수 있습니다.                            |
| 회원가입      | 회원가입은 어떤 웹사이트나 애플리케이션에 등록되어 그 서비스를 이용하기 위해 필요한 절차입니다. 일반적으로 사용자는 자신의 정보(이름, 이메일, 비밀번호 등)를 제공하여 계정을 생성하고, 해당 서비스를 이용할 수 있는 권한을 얻게 됩니다. 회원가입을 통해 사이트에 로그인하여 서비스를 사용하거나 특정 기능에 접근할 수 있게 됩니다.                                 |
| 로그인        | 등록된 유저 계정으로 시스템에 접근하여 유저 식별을 수행하는 과정입니다.                                                                                                                                                                                                                                                                                            |
| 디깅(Digging) | 디깅이란 원래 디제이가 자신의 공연 리스트를 채우기 위해서 음악을 찾는 행위를 의미하나, 현재는 자신의 특색있는 플레이리스트를 짜는 것으로 그 의미가 확대 되어 일반인들도 사용하는 언어입니다.                                                                                                                                                                       |
| ChatGPT       | ChatGPT란 OpenAI가 개발한 대형 언어 모델(large language model, LLM) 챗봇을 뜻합니다. ChatGPT는 대화 형태로 상호작용을 하며 놀라울 정도로 인간과 대화하는 것과 같은 반응을 제공하는 능력을 가지고 있습니다.                                                                                                                                                         |

#### 문서 개요

해당 문서는 **뮤딕**의 웹 페이지의 개발과 관련된 주요 정보를 다룹니다. 여기에는 주로 개발자를 위한 기능적 요구사항과 기술적 용어로 작성된 서비스의 세부 기능에 관한 내용이 포함됩니다.

<a href="https://docs.google.com/spreadsheets/d/1k1bcUxAqGr-WbKBvex_J7M51-aIQd9EQxcZN1uKBqaY/edit?pli=1#gid=0"><img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/15c6d0e7-358a-4838-884c-d47dc6228103"/></a>

<!-- ![스크린샷 2024-01-07 154023](https://github.com/MusicDigging/Mudig_BE/assets/107661525/15c6d0e7-358a-4838-884c-d47dc6228103) -->

### 3.3. API 명세서

#### 3.3.1. API 명세서: https://api.mudig.co.kr/api/swagger/

![스크린샷 2023-12-17 215443](https://github.com/MusicDigging/Mudig_BE/assets/107661525/c1e41600-d0c4-476d-8615-b71b72fc6df5)
![스크린샷 2023-12-25 195931](https://github.com/Hyunwooz/Django_Channels_Practice/assets/107661525/8c02ae00-7087-4c91-a23a-0ce12a184f3e)

### 3.4. URL 설계

#### api.mudig.co.kr

| 기능                          | URL                                       | Method | 담당   |
| ----------------------------- | ----------------------------------------- | ------ | ------ |
| USER                          |                                           |        |        |
| 이메일 인증                   | /user/otp                                 | POST   | 김여주 |
| 닉네임 중복 검사              | /user/checkname                           | POST   |        |
| 회원가입                      | /user/join                                | POST   |        |
| 로그인                        | /user/login                               | POST   |        |
| 로그아웃                      | /user/logout                              | POST   |        |
| 소셜 로그인                   | /user/login/{provider}                    | GET    |        |
| 소셜 로그인 콜백              | /user/login/{provider}/callback           | POST   |        |
| 소셜 회원 가입                | /user/socialjoin/                         | POST   |        |
| 비밀번호 변경                 | /user/changepassword                      | PUT    |        |
| 회원 탈퇴                     | /user/withdrawal                          | DELETE |        |
| 프로필 조회                   | /user/profile                             | GET    | 심민정 |
| 타 유저 프로필 조회           | /user/profile/<int:user_id>               | GET    |        |
| 프로필 수정                   | /user/profile/edit                        | PUT    |        |
| 팔로우                        | /user/<int:user_id>/follow                | POST   |        |
| 언팔로우                      | /user/<int:user_id>/unfollow              | DELETE |        |
| 팔로워 목록 조회              | /user/<int:user_id>/followers             | GET    |        |
| 팔로잉 목록 조회              | /user/<int:user_id>/following             | GET    |        |
| PLAYLIST                      |                                           |        |        |
| 플리 조회                     | /playlist                                 | GET    | 황봉수 |
| 플리 생성                     | /playlist/create                          | POST   |        |
| 플리 삭제                     | /playlist/delete/<int:playlist_id>        | DELETE |        |
| 플리 수정                     | /playlist/detail/<int:playlist_id>/edit   | PUT    |        |
| 플리 상세보기                 | /playlist/detail/<int:playlist_id>        | GET    |        |
| 기존 플리에 곡 추가           | /playlist/add                             | PUT    |        |
| 내 플리 보기 (음악추가 할 때) | /playlist/myplaylist                      | GET    |        |
| 모든음악 (음악추가할 때)      | /playlist/music                           | GET    |        |
| 플리 검색                     | /playlist/search?query={string}           | GET    | 사수봉 |
| 플리 좋아요                   | /playlist/like                            | POST   |        |
| 플리 댓글 작성                | /playlist/comment/write                   | POST   |        |
| 플리 대댓글 작성              | /playlist/recomment/write                 | POST   |        |
| 플리 댓글 수정                | /playlist/comment/edit                    | PUT    |        |
| 플리 댓글 삭제                | /playlist/comment/delete/<int:comment_id> | DELETE |        |
| 랜덤 뮤비                     | /playlist/random-mv                       | POST   | 강현우 |
| 이벤트성 플리 생성            | /playlist/event                           | POST   |        |

### 3.5. 프로젝트 설계 및 프로세스

#### 3.5.1. Architecture

![스크린샷 2023-12-25 171731](https://github.com/MusicDigging/Mudig_BE/assets/107661525/77308022-693e-409a-a76d-ff640530228b)

#### 3.5.2. 폴더 트리

```
📦Mudig_BE
 ┣ 📂.github
 ┃ ┗ 📂workflows
 ┃ ┃ ┗ 📜main.yml
 ┣ 📂mudig
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂playlist
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜gpt.py
 ┃ ┣ 📜karlo.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜playlist_utill.py
 ┃ ┣ 📜prompt.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜uploads.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┣ 📜youtube.py
 ┃ ┗ 📜__init__.py
 ┣ 📂user
 ┃ ┣ 📂migrations
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📂user
 ┃ ┃ ┃ ┗ 📜email_template.html
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜utils.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.gitignore
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
```

### 3.6. 개발 일정

#### 3.6.1. 개발 일정

##### 개발 기간

- 2023.11.03 ~ 2023.12.29

##### 회의록

- 프로젝트 회의록 : https://www.notion.so/Mudig-4de021314fe54804a03d291908f3d508

![스크린샷 2023-12-17 220226](https://github.com/MusicDigging/Mudig_BE/assets/107661525/c2f07559-6668-4d91-8e84-b051e45474d9)

##### 일정 관리

- 일정 관리: https://github.com/orgs/MusicDigging/projects/2/views/1

![스크린샷 2023-12-25 143942](https://github.com/Hyunwooz/kokoaTalkClone/assets/107661525/645997da-5bb7-4473-b7f7-fa4a59fcbf43)
![스크린샷 2023-12-25 143950](https://github.com/Hyunwooz/kokoaTalkClone/assets/107661525/d60e3ae0-339c-4627-9574-6820283aae01)

### 3.7. Git Branch 전략

Stable - Main (release) - Develop - 작업자별 Branch

#### 3.7.1. 각 브랜치별 설명

```
1. Stable : 서버 배포 단계에서 안정화된 버전
2. Main : 서버 배포 단계
3. Develop : 각 작업자별 브랜치에서 기능 개발 후 병합 및 디버깅 진행
4. 작업자별 Branch : 각자 맡은 기능 개발
```

#### 3.7.2. 작업 흐름

1. 작업자별 Branch 생성 후 기능 개발 진행
2. Develop Branch로 Push
3. Develop Branch 병합 후 디버깅 진행
4. Develop에서 메인 브랜치에 Push
5. 서버 배포 진행

## 4. 기능 ( 유저 피드백 반영 후 리뉴얼 예정 )

<table>
  <thead>
    <tr>
      <th align="center">플레이리스트 생성</th>
      <th align="center">플레이리스트 삭제</th>
      <th align="center">플레이리스트 상세보기</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/00e69961-5d5a-40e7-996d-a420a2031e70" height="462" style="max-width: 206px; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/89c34fdf-f8a7-4732-ab86-7db9fb3aa116" height="462" style="max-width: 206px; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/805cd361-35bb-4b3b-b3f3-276704ef69ad" height="462" style="max-width: 206px; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">플레이리스트 제목 수정</th>
      <th align="center">플레이리스트 곡 이동</th>
      <th align="center">플레이리스트 곡 삭제</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/0e4ad205-5bb7-4b23-9123-bf2796aeeffb" height="462" style="max-width: 206px; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/d2e0548c-0db9-4fc8-bf39-15cdd03de11c" height="462" style="max-width: 206px; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/da8f6e1a-d0f7-4965-b8de-3dc6d86c64d6" height="462" style="max-width: 206px; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">자체로그인</th>
      <th align="center">카카오로그인</th>
      <th align="center">로그아웃</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/43a66c38-f18c-47fb-a317-083df6a48794" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/5d9d45d9-43f0-482e-a676-5ab166ac5837" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/85fbb02e-2243-4827-bc0f-a20987d25d4a" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">회원가입</th>
      <th align="center">이메일인증</th>
      <th align="center">회원가입 후 프로필 생성</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/57975a0e-744b-4dc5-bebf-97470fb57e16" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/a7b68395-1388-4627-b3e8-b89dcdc336d2" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/106c9347-0c7e-45ea-9d88-4ac63bcaa26e" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">회원 탈퇴</th>
      <th align="center">랜덤 뮤비</th>
      <th align="center">이벤트 플리 생성</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/21ab6c71-6ebe-4cf1-a4ec-4a29f2d65773" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/7af72fd3-9d4d-428f-9452-2ea8ce88a54f" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/91625a11-e2bc-4fab-b3f8-a564e9d98cbc" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">프로필 조회</th>
      <th align="center">프로필 수정</th>
      <th align="center">팔로우 목록 조회</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/1038fcf0-2af5-4c9d-bf03-55bcfd7e0e76" height="462" style="max-width: 206px; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/17a92c43-36ca-4e9c-9190-c5f002b9a897" height="462" style="max-width: 206px; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/cc4b8e50-e129-4d62-9bea-8df31e1283ca" height="462" style="max-width: 206px; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">팔로우</th>
      <th align="center">언팔로우</th>
      <th align="center">유저 검색</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/20312da2-9662-4463-831f-9cfe3ea413bc" height="462" style="max-width: 206px; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/196bf2af-d8a4-4437-89ee-6aedeb8934bc" height="462" style="max-width: 206px; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/81991b06-21a7-456f-80e5-9777a5e5d063" height="462" style="max-width: 206px; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">플리 검색 및 좋아요</th>
      <th align="center">댓글 조회</th>
      <th align="center">댓글 생성</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/48f9e06f-3afc-4d1f-81ee-150405003da2" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/84dd064d-8041-4b1e-b0ae-98c2781088f7" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/a88dac6f-3867-425d-a05e-4875a9607976" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">댓글 수정</th>
      <th align="center">댓글 삭제</th>
      <th align="center">답글(대댓글) 조회</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/2671fb91-2e90-45b8-81ed-9ebb9c4b37fc" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/f9584a46-8ed9-4de5-a142-ea932fde41bd" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/18871040-688e-495b-a600-a3523dec6de9" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">답글(대댓글) 생성</th>
      <th align="center">답글(대댓글) 수정</th>
      <th align="center">답글(대댓글) 삭제</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/b2cc2386-4669-4bc8-b8d6-5becca342af2" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/1e3a9c38-6aaa-4a60-8274-66e143c97ed0" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/23b9b50c-f1d8-4106-8207-eb080ed75eb3" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

## 5. 개발하며 느낀점

### 5.1. 배운 점

#### 5.1.1 Open Api Specification

#### 5.1.2 CI/CD

Discord 웹 훅을 이용한 배포 메시지

#### 5.1.3 RESTfull API

##### **REST API란**

REST의 원리를 따르는 API를 말합니다.

```
💡 REST란
1. HTTP URI를 통해 자원을 명시하고
2. HTTP Method(Post,Get,Put,Delete)를 통해
3. 해당 자원에 대한 *CRUD Operation을 적용하는 것을 의미합니다.
```

**Rest의 구성 요소**

1. 자원 : HTTP URI
2. 자원에 대한 행위 : HTTP Method
3. 자원에 대한 행위의 내용 : HTTP Message Pay Load

**CRUD Operation**

```
컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리기능을 묶어서 일컫는 말입니다.
```

##### REST API 설계

1. URI는 동사보다는 명사, 대문자보다는 소문자
2. 마지막에 슬래시를 포함하지 않는다.
3. 언더바 대신 하이폰
4. 파일확장자는 포함하지 않는다.
5. 행위를 포함하지 않는다.

##### 장점

REST API 메시지가 의도하는 바를 명확하게 나타내므로 그 의도를 쉽게 파악할 수 있습니다.
서버와 클라이언트의 역할을 명확하게 분리할 수 있습니다.

**RESTful**

REST의 원리를 따르는 시스템을 의미합니다. REST API의 설계 규칙을 올바르게 지킨 시스템을 RESTful 하다 말할 수 있습니다.

**특징**

1. 서버와 클라이언트 구조
2. Stateless
3. Cacheable (캐시처리 가능)
4. 계층화
5. 인터페이스의 일관성

#### 5.1.4 OAuth

##### **OAuth(Open Authorization)란**

OAuth(Open Authorization)은 웹 및 애플리케이션 보안 프로토콜로, 인터넷 사용자의 데이터 및 서비스를 안전하게 제3의 애플리케이션에 제공하는 데 사용됩니다. 다른 서비스나 애플리케이션의 접근을 허용하는 인증 및 권한 부여 프레임워크로 작동합니다.

**OAuth의 구성 요소**

1. Resource Owner : 말 그대로 리소스 소유자이며, 애플리케이션을 사용하는 사용자 입니다.
2. Resource Server : 사용자의 리소스를 가지고 있으며, 클라이언트에 제공해주는 서버로, 구글이나 페이스북과 같은 플랫폼을 생각하시면 됩니다.
3. Client : 리소스에 접근하려는 애플리케이션 입니다
4. Authorization Server : 클라이언트가 리소스 서버에 있는 리소스에 접근할 때 필요한 Access Token을 제공하는 서버입니다.

### 5.2. 느낀 점

#### 강현우

이번 프로젝트를 통해 기획의 중요성에 대해서 크게 깨닫게 된 것 같습니다.
기획의 완성도가 개발 진행 속도에 많은 관여를 한다는 걸 느낀 프로젝트 였습니다.
프론트엔드, 디자이너 분들과 협업할 수 있었던 좋은 기회였습니다.
매주 회의를 통해 서로 필요한 부분에 대해서 대화를 나누고 오류를 같이 해결해 나가는 즐거운 경험을 할 수 있었습니다.
추후에 다른 개발자분, 디자이너분들과 의사소통을 하더라도 이번 프로젝트를 경험삼아 의사소통을 잘 이어나갈 수 있을 것 같습니다.
이번 프로젝트는 처음으로 도입하는 기술들이 여러개 있었습니다.
Open Api Specification를 통해 API 문서 자동화를 도입한다던가 Github Action을 통한 CI/CD 구현 등등 처음 다루는 기술들이라 조금 많이 서툴었지만,
Open Api Specification을 프론트엔드 분들이 너무 잘사용해주셔서 엄청난 뿌듯함을 느낄 수 있었습니다. 이번 프로젝트를 바탕으로 더욱 더 성장하는 개발자가 되도록 하겠습니다.
마지막으로 백엔드 총괄이라는 역할로 이번 프로젝트를 이끌었지만 많이 부족한 저를 너무나도 잘 따라주셔서 감사했습니다.
저와 함께 이번 프로젝트를 진행해주신 우리 뮤딕팀 분들!! 프론트, 백엔드, 디자이너분들 너무나도 고생많으셨습니다. 감사합니다.

#### 김여주

이번 Mudig 프로젝트를 통해 원활한 의사소통의 중요성과 팀워크의 힘을 다시 한번 느낄 수 있었습니다.
매주 회의를 통한 소통은 프로젝트를 진행하는데 변수가 발생할 때마다 신속한 해결을 가능케 하였고, 이는 기획의 완성도를 높이는 중요한 과정이었습니다. 프로젝트 진행 상황, 작업 일정, 오류 등을 소통함으로써 기획을 보다 세밀하게 계획하고 진행할 수 있었습니다.
이번 프로젝트에서 맡은 기능은 이전에 시도해보지 않았던 사용자 기능이었습니다. 회원가입, 로그인, 소셜로그인(카카오, 구글), 이메일 인증번호, 비밀번호 변경, 회원탈퇴 기능을 담당하게 되었고, 이를 통해 사용자 기능에 대한 로직의 흐름을 정확히 이해하게 되었습니다.
사용자의 기능에서 디테일하게 처리해야 하는 부분이 생각보다 많았습니다. 사용자가 입력한 프로필 이미지, 닉네임, 소개, 장르 등을 데이터베이스에 저장할 때 이미지의 존재 여부와 잘못된 정보에 대한 처리 등 디테일한 부분을 고려하여 구현하였습니다. 또한 프론트엔드 팀과의 의사소통을 통해 프론트엔드에서 보여질 응답 메시지와 디테일한 부분도 고려하여 코드를 작성하게 되었습니다. 프론트엔드 팀과의 협업을 통해 코드 수정 사항을 빠르게 확인하고 반영할 수 있었으며, 이러한 빠른 피드백과 협업은 개발 속도를 향상시키고 완성도를 높일 수 있었습니다.
처음에는 새로운 기능을 맡는 것에 대한 걱정이 있었지만, 어려웠던 부분에서 자신의 파트가 아님에도 같이 문제를 해결할 수 있도록 도와주는 팀원들이 있었기에 자신감을 가지고 끝까지 프로젝트를 마무리 할 수 있었습니다. 우리 백엔드 팀원들 감사합니다 !!
마지막으로 디자이너 팀, 프론트엔드 팀, 백엔드 팀 Mudig 구성원 모두 수고하셨고 프로젝트 하는 동안 행복했습니다 !!

#### 사수봉

이번 뮤딕 프로젝트를 디자이너, 프론트엔드 분들과 함께 진행하면서 협업은 소통이 중요하다는 것을 다시 한번 배웠습니다. 매주 다 같이 모여서 회의를 같이 진행해도 기능 하나하나를 만들어가는 과정에서는 빠른 소통과 피드백이 필요했는데 처음에는 이 부분이 쉽지 않았지만 프로젝트가 진행될수록 서로의 파트에 이해도가 생기면서 유연하게 작업을 진행할 수 있었습니다. 또한 자세한 기획의 중요성을 알게 되었습니다. 처음에는 완벽해 보였던 기획이 프로젝트를 진행하면서 여러 번 수정되는 걸 경험하면서 처음부터 완벽하진 않아도 디테일한 요소들을 자세하게 기획하는 것이 초반에는 시간이 소요되더라도 길게 보면 효율적인 진행 방법이라는 것을 배웠습니다.이번 프로젝트에서 검색과 댓글과 대댓글 CRUD, 플레이리스트 좋아요 기능을 담당하게 되었는데 처음에는 지난 프로젝트 개발 코드들과 별다를 게 없을 거라고 생각했지만 막상 작업을 진행할수록 같은 메소드를 비슷한 기능에 사용하더라도 디테일이 매우 다르다는 것을 새삼 느꼈습니다.디자이너, 프론트엔드 분들과 협업한 프로젝트는 이번이 처음인데 너무나도 뛰어나신 팀원분들을 만나서 제 능력 이상의 결과물을 만날 수 있었습니다. 부족한 제 실력에도 멋진 프로젝트의 마지막까지 완주할 수 있게 도와주신 모두 감사합니다!

#### 심민정

처음으로 프론트엔드, 디자이너 분들과 협업으로 진행하는 프로젝트였고, 부트캠프가 아닌 자율적으로 참여하는 프로젝트 였습니다.
그래서 실력에 대해 자신감이 많이 부족해서 "내가 실수하거나 못하면 어떡하지" 라는 걱정이 앞섰는데 팀원들의 격려로 프로젝트에 참여하게 되었고, 결론적으로 한층 더 성장할 수 있는 경험을 얻었다고 생각합니다.

제가 맡은 포지션은 프로필 CRUD, 팔로우 기능, 조회 기능 등이 있습니다.
처음 포지션을 분배할 때 전에 해봤던 로그인, 회원가입을 하려고 했으나, 팀원들의 권유와 새로운 것에 도전하는 것이 좀 더 흥미롭고 성장하는데 도움이 될 것 같아 위와 같은 포지션을 맡았습니다.

어려웠던 점은 프로필 수정부분에서 이미지 처리 방식을 장고 s3에 저장하도록 했는데 이 부분은 팀원분의 도움이 없었으면 사용하지 못했을 것 같습니다. 또한 데이터를 보내줄때도 프론트엔드 분들의 요구에 부합하도록 끊임없는 수정작업이 필요했습니다.
그러나 이러한 어려운 점은 매 주 회의를 통한 의견소통과 합의점을 찾아가면서 점차 맞춰나가는 과정이 있었기 때문에 힘 들기보다는 오히려 수정 후 원하는 방향대로 코드가 동작하거나 결과물이 모양을 갖춰나가는 부분에서 큰 희열감과 즐거움을 느낄 수 있었습니다.

마지막으로 막힐 때마다 함께 해결해주려던 우리 백엔드 팀원분들과 적극적으로 소통 해주신 프론트엔드, 디자이너분들 정말 수고많으셨습니다!

#### 황봉수

항상 팀 프로젝트를 함으로써 느끼는 거는 의사소통의 중요성인 거 같다. 처음으로 프론트엔드 분들과 디자이너분들과 협업하여 진행하였는데 의사소통이 충분하다고 생각하였지만 생각보다 더 많은 의사소통이 필요했고, 기획자의 역할 또한 중요하다고 생각하였습니다. 모두가 기획자가 되어 필요 순서에 따라 진행한 점은 만족하고 있다. 진행하면서 매주 회의 또한 만족스러웠다. 회의와 소통을 함으로써 프론트엔드 분들과 기술적으로 필요한 부분을 전달해주는 과정에서 즐거움을 얻었다. 그리고 백엔드와 프론트엔드 업무를 나누면서 각 파트가 직면하는 어려움과 즐거움을 이해할 수 있었습니다. API와 연동하며 백엔드의 역할과 프론트엔드의 동작 원리를 더 자세히 이해할 수 있었습니다. 마지막으로 우리 백엔드 팀, 프론트엔드팀, 디자인팀 다들 너무 고생하셨습니다.

## 6. 외부 어플리케이션

### ChatGPT

ChatGPT란 OpenAI가 개발한 GPT-3.5 기반의  **대형 언어 모델(large language model, LLM)** 챗봇을 뜻합니다. ChatGPT는 대화 형태로 상호작용을 하며 놀라울 정도로 인간과 대화하는 것과 같은 반응을 제공하는 능력을 가지고 있습니다.

API 사용은 유료이며, 대화에 사용된 토큰(Tokens)의 크기(1,000토큰 당 $0.002(약 3원))에 따라 과금됩니다.

- **[API 사용요금](https://openai.com/pricing)**
  - Model: gpt-3.5-turbo
  - Usage: $0.002 / 1K tokens

**예제 코드**

```python
import openai

openai.api_key = '${API_KEY}'

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-3.5-turbo"
# 질문 작성하기
query = "Django에 대해서 공부를 시작하려는데, 계획 좀 세워줘"

# 메시지 설정하기
messages = [
    {"role": "system", "content": "너는 공부 계획을 세워주는 스터디 플래너야"},
    {"role": "user", "content": query}
]
# ChatGPT API 호출하기
response = openai.ChatCompletion.create(
    model=model,
    messages=messages
)
answer = response['choices'][0]['message']['content']

print(answer)
```

**결과**

```python
Django에 대한 공부 계획을 세워보겠습니다. 아래는 예시입니다.

1. Django 개요 및 설치
- Django의 개념과 특징을 학습합니다.
- Django를 설치하고 개발 환경을 구축합니다.

2. Django 기본 구조와 웹 개발 기초
- Django 프로젝트와 앱의 구조를 이해합니다.
- URL 패턴, 뷰, 템플릿을 사용하여 간단한 웹 페이지를 개발합니다.

3. Django 모델과 데이터베이스
- Django의 모델을 사용하여 데이터베이스를 설계합니다.
- 데이터베이스 마이그레이션을 작업하여 데이터를 관리합니다.

4. Django 관리자 페이지
- Django의 내장된 관리자 페이지를 사용하여 데이터를 관리합니다.
- 커스텀 모델 관리자 및 인증과 권한 설정을 학습합니다.

5. Django 폼과 사용자 인증
- Django 폼을 사용하여 사용자 입력을 처리합니다.
- Django의 사용자 인증 기능을 이용하여 사용자 로그인, 회원가입, 로그아웃 등을 구현합니다.

6. Django 템플릿과 정적 파일
- Django 템플릿을 사용하여 동적인 웹 페이지를 생성합니다.
- 정적 파일(이미지, CSS, JavaScript 등)을 처리하는 방법을 학습합니다.

7. Django REST framework를 이용한 API 개발
- Django REST framework를 사용하여 RESTful API를 개발합니다.
- API에 대한 인증, 권한 설정 등을 구현합니다.

8. Django 데이터베이스 활용
- 다양한 데이터베이스 기능을 사용하여 데이터 조작 및 쿼리를 수행합니다.
- 데이터베이스 성능 최적화 방법을 학습합니다.

9. Django 테스트 및 디버깅
- Django의 테스트 프레임워크를 사용하여 유닛 테스트를 작성합니다.
- 디버깅 도구를 활용하여 오류를 찾아 수정하는 방법을 학습합니다.

10. Django 배포와 운영
- Django 프로젝트를 서비스 환경으로 배포하는 방법을 학습합니다.
- 서버 설정, 보안 강화, 성능 향상을 위한 최적화 작업을 수행합니다.

이렇게 계획을 세워보시고, 각 단계마다 필요한 참고 자료나 책을 구해서 공부하시면 됩니다. 도움이 되었길 바랍니다!
```

### Karlo

Karlo API는 사용자가 입력한 문장과 이미지를 기반으로 새로운 이미지를 만드는 기능을 제공합니다. 생성형 인공지능(Artificial Intelligence, AI) Karlo는 3억 장 규모의 이미지-텍스트 학습을 통해 사용자가 묘사한 내용을 이해하고, 픽셀 단위로 완전히 새로운 이미지를 빠르게 생성합니다. 또한 사용자가 원하는 콘셉트에 맞춰 창작 활동을 할 수 있도록 사물, 배경, 조명, 구도, 다양한 화풍을 지원합니다.

**이용 제한**

| 시간 | 제한                        |
| ---- | --------------------------- |
| 분당 | 결과 생성 수 기준 30건      |
| 일간 | 결과 생성 수 기준 3,000건   |
| 월간 | 결과 생성 수 기준 600,000건 |

**예제 코드**

```python
# REST API 호출, 이미지 파일 처리에 필요한 라이브러리
import requests
import json
import urllib
from PIL import Image

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
REST_API_KEY = '${REST_API_KEY}'

# 이미지 생성하기 요청
def t2i(prompt, negative_prompt):
    r = requests.post(
        'https://api.kakaobrain.com/v2/inference/karlo/t2i',
        json = {
            'prompt': prompt,
            'negative_prompt': negative_prompt
        },
        headers = {
            'Authorization': f'KakaoAK {REST_API_KEY}',
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response

# 프롬프트에 사용할 제시어
prompt = "A cat with white fur"
negative_prompt = "sleeping cat, dog, human, ugly face, cropped"

# 이미지 생성하기 REST API 호출
response = t2i(prompt, negative_prompt)

# 응답의 첫 번째 이미지 생성 결과 출력하기
result = Image.open(urllib.request.urlopen(response.get("images")[0].get("image")))
result.show()
```

**결과**

![sample.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/ff831e0d-89cf-407e-92f6-76f7f4ac37ee/6a5858bc-fd51-435a-a16c-702d5425c4a6/sample.png)

### Youtube Data API

YouTube Data API를 사용하면 YouTube 웹사이트에서 일반적으로 실행되는 기능을 자신의 웹사이트 또는 애플리케이션에 통합할 수 있습니다. 아래 목록은 API를 사용하여 검색할 수 있는 다양한 유형의 리소스를 식별합니다. API는 이러한 리소스를 대부분 삽입, 업데이트, 삭제하는 메서드도 지원합니다.

[API Reference  |  YouTube Data API  |  Google for Developers](https://developers.google.com/youtube/v3/docs?hl=ko)

**API 호출**

1. 모든 요청은 API 키 (`key` 매개변수 포함)를 지정하거나 OAuth 2.0 토큰을 제공해야 합니다. API 키는 프로젝트의 [Developer Console](https://console.developers.google.com/?hl=ko)에 있는 **API 액세스** 창에서 확인할 수 있습니다.
2. 모든 삽입, 업데이트, 삭제 요청에 대해 **반드시** 승인 토큰을 전송해야 합니다. 또한 인증된 사용자의 비공개 데이터를 검색하는 모든 요청에 대해 인증 토큰을 보내야 합니다.

   또한 리소스를 가져오기 위한 일부 API 메서드는 인증이 필요한 매개변수를 지원하거나 요청이 인증될 때 추가 메타데이터를 포함할 수 있습니다. 예를 들어 사용자가 업로드한 동영상을 검색하는 요청에는 특정 사용자가 요청을 인증할 경우 비공개 동영상도 포함될 수 있습니다.

3. API는 OAuth 2.0 인증 프로토콜을 지원합니다. OAuth 2.0 토큰은 다음 방법 중 하나로 제공할 수 있습니다.

## 7. 유저 피드백 후 반영

### 검색 결과 - 음악 찾기 추가

### 프롬포트 결과 7~10개 랜덤 추가 , 뮤비 제목 15자 이내로, 설명은 3줄 이내로

### 비밀번호 찾기 기능 추가

### 플레이리스트 썸네일 이미지 변경 추가
