# Mudig

![mudig 캐릭터](https://github.com/Hyunwooz/kokoaTalkClone/assets/107661525/9aedcb7c-c93e-4eac-b9a8-9d1cd7de7789)

[뮤딕 바로가기](https://www.mudig.co.kr/)

```
해당 서비스를 이용해보실 수 있는 테스트 계정입니다.

 ID : mudig01@email.com
 PW : example

 ID : mudig02@email.com
 PW : example

 ID : mudig03@email.com
 PW : example

 ID : mudig04@email.com
 PW : example

 ID : mudig05@email.com
 PW : example
```

## 계기 및 목표

### 1️⃣ AI는 아직 사람들과 친해지지 않았다.

### 2️⃣ AI에 대한 부정적인 시선을 낮추고, 사람들과 친해지는 계기를 제공하자!

```
현재 AI 기술은 사람들에게 많은 관심을 받고 있지만 
아직도 많은 사람들과는 친해지지 않았습니다.

그래서 우리의 서비스를 통해 좀더 친해질 수 있는 기회를 제공하고 싶었습니다.
```

## 인삿말


안녕하세요. 🙇‍♂️

뮤딕(Mudig, Music Digging 이하 뮤딕)은 사용자들이 새로운 음악을 발견하고, 추천받으며, 공유할 수 있는 플랫폼을 말합니다.

GPT (Generative Pretrained Transformer) 기술과 Karlo(T2I, Text to Image)를 사용하여 개인화된 음악 추천과 인터렉티브한 경험을 제공하는 서비스입니다.

뮤딕은

1️⃣ 자체 회원가입 뿐만 아니라 구글, 카카오를 이용한 소셜 로그인을 지원하고 있습니다. <br>
2️⃣ 인공지능을 통해 새로운 음악을 찾는 즐거움을 드릴 수 있습니다.<br>
3️⃣ 자신만의 플레이리스트를 공유하고, 소통하며 무료한 일상에 소소함 즐거움을 느낄 수 있도록 장소를 제공해드립니다.

### 디깅이란?

```
‘디깅’이란 원래 디제이가 자신의 공연 리스트를 채우기 위해서 음악을 찾는 행위를 의미하나,
현재는 자신의 특색있는 플레이리스트를 짜는 것으로 그 의미가 확대 되어 일반인들도 사용하는 언어이다.
```

## 팀원 소개

### 안녕하세요. Team OrGo 입니다!

|                                                                         강현우                                                                         |                                                 김여주                                                 |                                                                                  사수봉                                                                                  |                                                 심민정                                                 |                                                                  황봉수                                                                   |
| :----------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://github.com/Hyunwooz/DjangoGptProject_FE/assets/107661525/722d5102-81f7-46a2-8afe-505595e57983" width="400" style="max-width: 100%;"> | <img src="https://avatars.githubusercontent.com/u/131739526?v=4" width="400" style="max-width: 100%;"> | <img src="https://cdn.discordapp.com/attachments/1141230189498617867/1147091272142692352/KakaoTalk_Photo_2023-09-01-17-46-40.jpeg" width="400" style="max-width: 100%;"> | <img src="https://avatars.githubusercontent.com/u/131655569?v=4" width="400" style="max-width: 100%;"> | <img src="https://cdn.discordapp.com/attachments/1141230189498617867/1147090595614031942/image.png" width="400" style="max-width: 100%;"> |
|                                                 <a href="https://github.com/Hyunwooz">🔗 Hyunwooz</a>                                                  |                         <a href="https://github.com/kimyeoju">🔗 kimyeoju</a>                          |                                                            <a href="https://github.com/su0797">🔗 su0797</a>                                                             |                           <a href="https://github.com/MJ-SIM">🔗 MJ-SIM</a>                            |                                             <a href="https://github.com/bnbbbb">🔗 bnbbbb</a>                                             |


안녕하세요 🙇‍♂️<br>
저희는 Mudig의 주니어 개발자 백엔드 팀 입니다.<br>
Estsoft에서 주관하는 백엔드 오르미 교육과정에서 만난 비전공자와 전공자들로 이루어져 있습니다.<br>
새로운 기술을 받아들임에 있어서 열린 마음을 가진 분들이 모여 프로젝트를 진행하였습니다.<br>
기술적으로 부족할 수도 있지만 최선을 다해 준비했습니다.<br>
잘부탁드립니다 :)

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

- 댓글과 대댓글 CRUD

  ```
  댓글을 이용하여 게시글에 대한 의견을 남길 수도 있으며 댓글의 대댓글 기능 까지 지원하고 있습니다.
  댓글을 수정, 삭제하는 기능까지 제공 되고 있습니다.
  ```

  <!-- [# 댓글 시연 영상](#55-댓글-기능) -->

- 기능 제목
  ```
  기능 설명
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
- AWS RDS

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

![스크린샷 2023-12-17 215443](https://github.com/MusicDigging/Mudig_BE/assets/107661525/c1e41600-d0c4-476d-8615-b71b72fc6df5)

### 3.3. URL 설계

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

### 3.4. 프로젝트 설계 및 프로세스

#### 3.4.1. Architecture

추가예정

#### 3.4.5. 폴더 트리

추가예정

### 3.5. 개발 일정

#### 3.5.1. 개발 일정

##### 개발 기간

- 2023.11.03 ~ 2023.12.00

##### 회의록

- 프로젝트 회의록 : https://www.notion.so/Mudig-4de021314fe54804a03d291908f3d508

![스크린샷 2023-12-17 220226](https://github.com/MusicDigging/Mudig_BE/assets/107661525/c2f07559-6668-4d91-8e84-b051e45474d9)

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

수정 예정

### 세부 페이지

Figma : https://www.figma.com/file/8jeAIfOdZcYZ8ehctmA8yn/Untitled?type=design&node-id=2-54&mode=design&t=DPLaDoTa3ZSmgwT4-0

수정 예정

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
