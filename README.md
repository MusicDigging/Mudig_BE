# Mudig

이미지 추가 예정

[뮤딕 바로가기](https://www.mudig.co.kr/)

```
해당 서비스를 이용해보실 수 있는 테스트 계정입니다.

 ID : example@email.com
 PW : example
```

## 계기 및 목표

### 1️⃣ AI는 아직 사람들과 친해지지 않았다.

```
현재 AI 기술은 많은 관심을 받고 있습니다. 하지만 아직도 AI 기술은 사람들과 친해지지 않았습니다.  그래서 친해질 수 있는 서비스를 제공하고 싶었습니다.
```

### 2️⃣ AI에 대한 부정적인 시선을 낮추고, 사람들과 친해지는 계기를 제공하자!

## 개요

```
안녕하세요. 🙇‍♂️

뮤딕은 사용자들이 새로운 음악을 발견하고, 추천받으며, 공유할 수 있는 플랫폼을 말합니다. GPT (Generative Pretrained Transformer) 기술을 사용하여 개인화된 음악 추천과 인터렉티브한 경험을 제공하는 서비스입니다.

1️⃣ 뮤딕은 자체 회원가입 뿐만 아니라 구글, 카카오를 이용한 소셜 로그인을 지원하고 있습니다.
2️⃣ 뮤딕은 새로운 음악을 찾는 즐거움을 드릴 수 있습니다.
3️⃣ 뮤딕은 자신만의 플레이리스트를 공유하고, 소통하며 즐거운 일상 생활을 즐길 수 있도록 장소를 제공해드립니다.
```

### 디깅이란?

```
‘디깅’이란 원래 디제이가 자신의 공연 리스트를 채우기 위해서 음악을 찾는 행위를 의미하나, 현재는 자신의 특색있는 플레이리스트를 짜는 것으로 그 의미가 확대 되어 일반인들도 사용하는 언어이다.
```

## 팀원 소개

### 안녕하세요. Team OrGo 입니다!

|                                                                         강현우                                                                         |                        김여주                         |                                                                                  사수봉                                                                                  |                      심민정                       |                                                                  황봉수                                                                   |
| :----------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/722d5102-81f7-46a2-8afe-505595e57983" width="400" style="max-width: 100%;"> |   <img src="" width="400" style="max-width: 100%;">   | <img src="https://cdn.discordapp.com/attachments/1141230189498617867/1147091272142692352/KakaoTalk_Photo_2023-09-01-17-46-40.jpeg" width="400" style="max-width: 100%;"> | <img src="" width="400" style="max-width: 100%;"> | <img src="https://cdn.discordapp.com/attachments/1141230189498617867/1147090595614031942/image.png" width="400" style="max-width: 100%;"> |
|                                                 <a href="https://github.com/Hyunwooz">🔗 Hyunwooz</a>                                                  | <a href="https://github.com/kimyeoju">🔗 kimyeoju</a> |                                                            <a href="https://github.com/su0797">🔗 su0797</a>                                                             | <a href="https://github.com/MJ-SIM">🔗 MJ-SIM</a> |                                             <a href="https://github.com/bnbbbb">🔗 bnbbbb</a>                                             |

저희는 Mudig의 주니어 개발자 백엔드 팀 입니다.
Estsoft에서 주관하는 백엔드 오르미 교육과정에서 만난 비전공자와 전공자들로 이루어져 있습니다. 앞서 설명드린 것 처럼 요즘 핫하다는 ChatGPT(LLM, AI 모델)를 이용하여 새로운 기술을 받아들임에 있어서 열린 마음을 가진 분들이 모였습니다! 항상 잘부탁드립니다 :)

### 협업 도구

📜 Notion , 📱 Discord

### 각자의 역할

## **[목차]**

1. [기능](#1-목표와-기능)
2. [개발 환경 및 배포 URL](#2-개발-환경-및-배포-URL)
3. [프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)
4. [전체 페이지](#4-전체-페이지)
5. [구현 기능 시연](#5-기능)
6. [개발하며 느낀점](#6-개발하며-느낀점)

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
  <!-- [# 유저 기능 시연 연상](#51-유저-기능) -->
- Follow / Unfollow 기능

  ```
  자신과 관심사가 비슷한 유저와 팔로워를 맺을 수 있습니다.
  ```

  <!-- [# 팔로우 시연 영상](#57-팔로우-기능) -->

- 댓글과 대댓글 CRD
  ```
  댓글을 이용하여 게시글에 대한 의견을 남길 수도 있으며 댓글의 대댓글 기능 까지 지원하고 있습니다.
  댓글을 수정, 삭제하는 기능까지 제공 되고 있습니다.
  ```
  <!-- [# 댓글 시연 영상](#55-댓글-기능) -->

## 2. 개발 환경 및 배포 URL

### 2.1. 개발 환경

- Python == 3.11.3
- Django == 4.2.4

AWS S3

- boto3 == 1.28.38

DRF

- djangorestframework == 3.14.0

### 2.2. 배포 환경

#### 2.2.1. Back-End

- Aws Ec2
- Nginx
  - wsgi : gunicorn
- AWS S3

### 2.3. 배포 URL

#### 2.3.1. Back-End

- https://api.mudig.co.kr/
- Back-End Repo : https://github.com/MusicDigging/Mudig_BE

#### 2.3.2. Front-End

- https://www.mudig.co.kr/
- Front-End Repo : https://github.com/MusicDigging/Mudig_FE

## 3. 프로젝트 구조와 개발 일정

### 3.1. Entity Relationship Diagram

![스크린샷 2023-10-17 145645](https://github.com/ESTsoft-OrGo/OrGo/assets/107661525/8d039f1e-aff5-42ed-9662-05201803bc1b)

[DB-Diagram 바로가기](https://dbdiagram.io/d/AIP-6548a0187d8bbd64658ecdfe)

### 3.2. API 명세서

#### 3.2.1. API 명세서: https://api.mudig.co.kr/api/swaggers

![스크린샷 2023-10-18 144438](https://github.com/ESTsoft-OrGo/OrGo/assets/107661525/9a23d9b3-38eb-441e-bc79-f6a5683d40bb)

### 3.3. URL 설계

#### api.mudig.co.kr

| 이름             | URL                           | Method    |
| ---------------- | ----------------------------- | --------- |
| User             |                               |           |
| 로그인           | user/login/                   | POST      |
| 소셜 로그인      | user/login/provider           | POST      |
| 회원가입         | user/join/                    | POST      |
| 이메일 OTP       | user/otp/                     | POST      |
| 프로필 조회      | user/profile/                 | GET       |
| 프로필 수정      | user/profile/update/          | PUT       |
| 비밀번호 변경    | user/profile/change-password/ | PUT       |
| 회원탈퇴         | user/profile/delete/          | DELETE    |
| Post             |                               |           |
| 게시글 조회      | post/                         | GET       |
| 게시글 작성      | post/write/                   | POST      |
| 게시글 수정      | post/edit/                    | PUT       |
| 게시글 삭제      | post/delete/                  | DELETE    |
| 게시글 상세보기  | post/view/                    | GET       |
| Search           |                               |           |
| 검색             | post/search/                  | GET       |
| Like             |                               |           |
| 좋아요           | post/like/                    | POST      |
| 좋아요 취소      | post/unlike/                  | DELETE    |
| Follow           |                               |           |
| 팔로잉/언팔로잉  | user/follow/                  | POST      |
| Comment          |                               |           |
| 쓰기             | post/comment/write/           | POST      |
| 삭제             | post/comment/delete/          | DELETE    |
| 대댓글 쓰기      | post/re-comment/write/        | POST      |
| Study            |                               |           |
| 목록             | study/?page=number            | GET       |
| 생성             | study/create/                 | POST      |
| 참가             | study/join/                   | POST      |
| 참가 취소        | study/join/cancle/            | DELETE    |
| 수정             | study/edit/                   | PUT       |
| 삭제             | study/delete/                 | DELETE    |
| tag 생성         | study/tag/write/              | POST      |
| tag 삭제         | study/tag/delete/             | DELETE    |
| Notify           |                               |           |
| 실시간 알림 받기 | notify/str:user_id/           | Websocket |
| 알림 목록        | notify/                       | GET       |

### 3.4. 프로젝트 설계 및 프로세스

#### 3.4.1. Architecture

![그림2](https://github.com/ESTsoft-OrGo/OrGoChat/assets/107661525/ea9b19ff-e6a9-425b-a0d1-ca8fa5fd54ff)

#### 3.4.5. 폴더 트리

```
📦OrGo
 ┣ 📂Orgo
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜wsgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┣ 📂chat
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜consumers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜routing.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜view.py
 ┣ 📂notify
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜consumers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜routing.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜view.py
 ┣ 📂post
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜uploads.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜view.py
 ┣ 📂study
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜uploads.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜pagination.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜view.py
 ┣ 📂user
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜uploads.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tokens.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜view.py
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
```

### 3.5. 개발 일정

#### 3.5.1. 개발 일정

##### 개발 기간

- 2023.11.03 ~ 2023.12.00

##### 회의록

- 프로젝트 회의록 : https://withorgo.notion.site/c7274b6b1f3e44579d1da91bfc771314?pvs=4

![스크린샷 2023-09-06 091325](https://github.com/Hyunwooz/DjangoGptProject_BE/assets/107661525/076839eb-94da-48ba-87fa-bcc264ba7657)

##### 일정 관리

- 일정 관리: https://withorgo.notion.site/d52779f12ac547dabc1240320ef4aeb2?v=fb0701095b3840218a980c13305cda34&pvs=4

![스크린샷 2023-09-04 175059](https://github.com/Hyunwooz/DjangoGptProject_BE/assets/107661525/cbe30798-aef7-4d7d-ac6a-5eda5d91b0c1)
![스크린샷 2023-09-01 141622](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/f9bae29d-0fbe-4e28-b771-2ef2dfe5c803)

프로젝트 고도화 일정

```
프로젝트 고도화는 Github Project를 이용하여 진행하였습니다.
```

- 프로젝트 고도화: https://github.com/orgs/ESTsoft-OrGo/projects/1

![스크린샷 2023-10-17 152908](https://github.com/ESTsoft-OrGo/OrGoChat/assets/107661525/782cb96c-c46d-4a4e-8346-4066cd735c26)

#### 3.5.2. 기술 스택

- Python
- Django
- KARLO (이미지 생성 AI)
- ChatGPT (LLM, 문장 생성 AI)

## 4. 전체 페이지

### 메인 페이지

![www withorgo site_index html (1)](https://github.com/ESTsoft-OrGo/OrGo/assets/107661525/78033f41-a08d-4681-ba5b-dc09927a9b72)

### 세부 페이지

Figma : https://www.figma.com/file/8jeAIfOdZcYZ8ehctmA8yn/Untitled?type=design&node-id=2-54&mode=design&t=DPLaDoTa3ZSmgwT4-0
![스크린샷 2023-09-02 112048](https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/2d97c668-c584-4225-b7fd-9b5f76ac746a)

## 5. 기능

## 6. 개발하며 느낀점

### 6.1. 배운 점

#### 6.1.1 배운 것 1

#### 6.1.2 배운 것 2

#### 6.1.3 배운 것 3

### 6.2. 개발중 만난 장애물과 극복 방법

### 6.3. 느낀 점

#### 강현우

내용

#### 김여주

내용

#### 사수봉

내용

#### 심민정

내용

#### 황봉수

내용

## 7. 유저 피드백 후 반영
