# Mudig

![296149697-a6800871-704b-4d56-b8ff-6fc6db0bcf72](https://github.com/MusicDigging/Mudig_BE/assets/107661525/64d3650a-0691-42c6-9f13-cfa1dbac1aa5)

[👉 뮤딕 바로가기](https://www.mudig.co.kr/)
[📌 뮤딕 개발 일지](https://voltaic-apricot-62e.notion.site/Mudig-4de021314fe54804a03d291908f3d508)

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
3. [기술 스택 및 배포 URL](#2-기술-스택-및-배포-url)
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
   a. [OpenAPI Specification](#511-openapi-specification)<br>
   b. [CI/CD](#512-cicd)<br>
   c. [Restful API](#513-restfull-api)<br>
   d. [Oauth](#514-oauth)
7. [외부 어플리케이션](#6-외부-어플리케이션)<br>
   a. [ChatGPT](#chatgpt)<br>
   b. [Karlo](#karlo)<br>
   c. [Youtube Data API](#youtube-data-api)<br>
8. [사용자 피드백 후 반영](#7-사용자-피드백)

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

##### Github Action을 통해 CI/CD 결과 알림 설정

구현 코드

```yml
# CI 성공 메세지 발송
build-CI-Success:
  needs: CI
  runs-on: ubuntu-latest
  if: success()
  steps:
    - name: Discord notification
      env:
        DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK }}
      uses: Ilshidur/action-discord@master
      with:
        args: "
          ## CI 진행\n

          ### 📌 Status\n
          > **Success** ✅\n

          ### ✍️ Commit message\n
          > ${{ github.event.commits[0].message }}\n"

# 배포 성공 메세지 발송
build-Deploy-Success:
  needs: deploy
  runs-on: ubuntu-latest
  if: success()
  steps:
    - name: Discord notification
      env:
        DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK }}
      uses: Ilshidur/action-discord@master
      with:
        args: "
          ## Deploy 진행\n

          ### 📌 Status\n
          > **Success** ✅\n

          ### ✍️ Commit message\n
          > ${{ github.event.commits[0].message }}\n

          ### 🫡 See changes\n
          > https://github.com/${{ github.repository }}/commit/${{github.sha}}\n"

# CI 실패 메세지 발송
build-CI-failure:
  needs: CI
  runs-on: ubuntu-latest
  if: failure()
  steps:
    - name: Discord notification
      env:
        DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK }}
      uses: Ilshidur/action-discord@master
      with:
        args: "
          ## CI 진행\n

          ### 📌 Status\n
          > **Failure** ⛔\n

          ### ✍️ Commit message\n
          > ${{ github.event.commits[0].message }}\n

          ### 👀 See Error Message\n
          > https://github.com/MusicDigging/Mudig_BE/actions\n"

#배포 실패 메세지 발송
build-Deploy-failure:
  needs: deploy
  runs-on: ubuntu-latest
  if: ${{ needs.deploy.outputs['result'] == 'failure' }}
  steps:
    - name: Discord notification
      env:
        DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK }}
      uses: Ilshidur/action-discord@master
      with:
        args: "
          ## Deploy 진행\n

          ### 📌 Status\n
          > **Failure** ⛔\n

          ### ✍️ Commit message\n
          > ${{ github.event.commits[0].message }}\n

          ### 👀 See Error Message\n
          > https://github.com/MusicDigging/Mudig_BE/actions\n"
```

## 1. 기능

### 1.1. 주요 기능

- 회원가입 및 로그인 , 소셜 로그인 (Kakao, Google)

  ```
  뮤딕 서비스는 이메일로 회원가입과 로그인을 기본으로 제공하며, 
  카카오와 구글을 활용한 소셜 로그인 기능을 추가하여 사용자가 서비스를 편리하게 이용할 수 있습니다. 
  또한, 마이 페이지에서는 비밀번호 변경, 회원탈퇴, 로그아웃과 같은 주요 기능을 제공하며 
  사용자의 계정 정보를 손쉽게 확인 및 수정할 수 있습니다.
  ```

- 이메일로 통한 회원가입시 메일 인증

  ```
  이메일로 회원가입 시, 보안을 강화하기 위해 SMTP 서버를 활용하여 
  메일 인증 기능을 구현했습니다. 사용자가 작성한 이메일 주소로 전송되는 인증번호를 
  통해서 사용자의 신원을 확인하고, 정확한 인증번호 입력 시에만 회원가입이 가능합니다.
  ```

- JSON Web Token 인증 방식

  ```
  로그인 시 발급된 Access Token을 활용하여 유저 인증을 수행하면서, 
  동시에 지속적인 세션 유지를 위해 Refresh Token을 제공합니다. 
  Refresh Token 갱신은 별도의 URL인 ‘api/token/refresh/‘ 를 통해 이뤄지며, 
  Access Token의 만료 전에 자동으로 새로운 Access Token을 획득합니다. 
  이로써 사용자는 로그인 상태를 지속하면서 Mudig 서비스를 보다 안전하게 즐길 수 있습니다.
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

## 2. 기술 스택 및 배포 URL

### 2.2. 기술 스택

<table>
<tr>
 <td align="center" width="100px">사용 기술</td>
 <td width="800px">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">&nbsp  
  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"/>&nbsp
  <img src="https://img.shields.io/badge/drf-B40404?style=for-the-badge&logo=django&logoColor=white"/>&nbsp 
    </td>
</tr>
<tr>
 <td align="center" width="100px">데이터베이스</td>
 <td width="800px">
  <img src="https://img.shields.io/badge/postgresql-3776AB?style=for-the-badge&logo=postgresql&logoColor=white">&nbsp  
    </td>
</tr>
<tr>
 <td align="center" width="100px">저장소</td>
 <td width="800px">
  <img src="https://img.shields.io/badge/amazon%20s3-CA4245?style=for-the-badge&logo=amazons3&logoColor=white"/>&nbsp   
    </td>
</tr>
<tr>
  <td align="center">배포</td>
  <td><img src="https://img.shields.io/badge/amazon%20ec2-232F3E?style=for-the-badge&logo=amazonec2&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/amazonaws%20rds-231F3E?style=for-the-badge&logo=amazonrds&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/NGINX-245432?style=for-the-badge&logo=NGINX&logoColor=white"></td>
</tr>
<tr>
 <td align="center" width="100px">API 문서</td>
 <td width="800px">
  <img src="https://img.shields.io/badge/Swagger-5FB404?style=for-the-badge&logo=swagger&logoColor=white">&nbsp  
    </td>
</tr>
<tr>
 <td align="center">협업</td>
 <td>
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"/>&nbsp 
    <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white"/>&nbsp
    <img src="https://img.shields.io/badge/Discord-4263f5?style=for-the-badge&logo=Discord&logoColor=white"/>&nbsp 
    <img src="https://img.shields.io/badge/Figma-d90f42?style=for-the-badge&logo=Figma&logoColor=white"/>&nbsp
 </td>
<tr>
 <td align="center">IDE</td>
 <td>
    <img src="https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white"/>&nbsp
</tr>
</table>

### 2.2. 배포 URL

#### 2.2.1. Back-End

- https://api.mudig.co.kr/
- Back-End Repo : https://github.com/MusicDigging/Mudig_BE

#### 2.2.2. Front-End

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

## 4. 기능
<table>
  <thead>
    <tr>
      <th align="center">이메일 회원가입</th>
      <th align="center">카카오 회원가입</th>
      <th align="center">구글 회원가입</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/268dbb22-c04b-4f10-bc7e-ce9deedca30e" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/08db6240-9139-4305-8916-6b02edab2701" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/e7bc6b81-709b-4a1a-b7f6-fc773b70c02c" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">이메일 로그인</th>
      <th align="center">카카오 로그인</th>
      <th align="center">구글 로그인</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/4423f0a5-909e-4a28-bfbd-882037c83bea" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/dbe70e1c-a8b1-4cb9-a374-6760b13b2e5b" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/b8d51317-b63c-4353-a600-5bb1fb258a5e" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">로그아웃</th>
      <th align="center">회원탈퇴</th>
      <th align="center">비밀번호 변경</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/b35d3b4e-537e-4ee5-81e1-48ebdedf259f" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/675e32e4-19d6-461d-bad0-70f88ef63436" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/88e0b5ea-55de-43a8-a169-6ed04822a7cf" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">팔로우 언팔로우</th>
      <th align="center">팔로우 팔로잉 목록</th>
      <th align="center">아더 프로필</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/207b21c1-88f4-4f91-b53c-70e230d90d68" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/83f58178-b667-43c8-8fa0-37c34aa32659" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/45aac933-6a04-4786-82b3-b217b581a99f" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">마이 페이지</th>
      <th align="center">프로필 수정</th>
      <th align="center">메인 페이지</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/cb87477f-a4bf-4a3c-8684-c28c1ddbace4" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/1a75e5fd-0df2-496d-bf4c-cd516324cc83" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/c1cf9cf4-729c-4c9b-aabd-545968ab97c9" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

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
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/5eeab5bd-a132-404d-8cc1-caf4a70cea38" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/3ca2bf8d-6ca8-47ca-ac84-99e2b9e5365d" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/ea349f30-802d-4c2b-99b3-6a86ae6c39c6" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">플레이리스트 수정</th>
      <th align="center">플레이리스트 좋아요</th>
      <th align="center">이벤트 플리 생성</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/2dcee812-16f3-43a5-b5c1-4d5d5adc73a2" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/be6ab0ed-e940-4587-a2bd-5c4d07e07cb1" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/1c9adc91-c549-40f6-87ec-b3f1645a09d1" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>



<table>
  <thead>
    <tr>
      <th align="center">플리/뮤직/유저 검색</th>
      <th align="center">댓글 CRUD</th>
      <th align="center">대댓글 CRUD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/4852e6d4-89e0-4a09-becb-8430c6e45392" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/598312f4-a9b3-494d-a244-1f2c4f1ad2aa" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/57ef9bb7-4683-4791-8041-3d67fba1db5d" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th align="center">랜덤 뮤비</th>
      <th align="center">곡 추가</th>
      <th align="center">스플래쉬</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/c08bab76-edde-442a-ab35-7a5db3af4472" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/8654ce8d-ab2b-4123-969e-2770d8087596" height="462" style="max-width: 100%; display: inline-block;">
      </td>
      <td align="center">
        <img src="https://github.com/MusicDigging/Mudig_BE/assets/107661525/5b2748dd-0167-4a80-bebe-428f22a8eab9" height="462" style="max-width: 100%; display: inline-block;">
      </td>
    </tr>
  </tbody>
</table>

## 5. 프로젝트를 진행하며

### 5.1. 배운 점

#### 5.1.1 OpenAPI Specification

##### OpenAPI Specification이란?

OpenAPI Specification은 웹 서비스 API를 설명하고 문서화하는 데 사용되는 표준화된 형식을 말합니다.
이해할 수 있는 API 설명을 제공함으로써 클라이언트 및 서버 간의 통신을 용이하게 만듭니다.

##### OpenAPI Specification 특징

1. OpenAPI Specification은 주로 YAML 또는 JSON 형식으로 작성됩니다. 이는 API 설명을 쉽게 작성하고 읽을 수 있도록 합니다.
2. OpenAPI Specification은 API의 엔드포인트, 매개변수, 응답 형식 등을 문서화하는 데 사용됩니다. 이는 개발자가 API를 어떻게 사용해야 하는지 이해하고 효율적으로 활용할 수 있게 합니다.
3. OpenAPI Specification은 주로 RESTful API를 설명하기 위해 사용됩니다. 이는 HTTP를 기반으로 하는 웹 서비스를 위한 표준적인 디자인 원칙을 따르는 API를 설계할 때 유용합니다.
4. OpenAPI Specification을 사용하면 API를 호출하는 데 필요한 서버 및 클라이언트 코드를 자동으로 생성할 수 있습니다. 이는 개발자가 API를 더 쉽게 통합할 수 있도록 도와줍니다.
5. 다양한 도구와 프레임워크에서 OpenAPI Specification을 활용하여 API를 자동으로 문서화하고 테스트하는 등의 작업을 수행할 수 있습니다. **저희 서비스의 경우 Swagger를 사용하였습니다.**
6. OpenAPI Specification은 API의 버전을 관리하는 데 도움이 됩니다. API가 업데이트되면 새로운 버전의 명세를 작성하여 이전 및 현재 버전 간의 차이를 명확히 할 수 있습니다.

OpenAPI Specification은 API 설계, 문서화, 구현, 테스트 및 유지 보수를 효과적으로 지원하는 표준화된 방법을 제공합니다. 이는 팀 간의 협업을 용이하게 하고 개발자가 API를 빠르게 이해하고 효과적으로 활용할 수 있도록 돕는 역할을 합니다.

#### 5.1.2 CI/CD

##### **지속적인 통합과 지속적인 배포 (CI/CD, Continuous Integration/Continuous Deployment)란**

CI/CD (Continuous Integration/Continuous Delivery)란 애플리케이션 개발 과정을 자동화하여 빠른 주기로 고객에게 서비스를 제공하는 방법을 말합니다.
CI/CD의 기본 개념은 지속적인 통합, 지속적인 서비스 제공, 지속적인 배포입니다.
특히, CI/CD는 애플리케이션의 통합 및 테스트 단계에서부터 제공 및 배포에 이르는 애플리케이션의 라이프사이클 전체에 걸쳐 지속적인 자동화와 지속적인 모니터링을 제공합니다.

##### **지속적인 통합 (Continuous Integration, CI)**

CI를 간단하게 말하자면, 빌드/테스트를 자동화 하는 과정을 말하며 개발자를 위한 지속적인 통합을 의미합니다.

개발자가 단위별로 구현한 부분을 병합할 때마다 자동화된 빌드와 테스트 실행되며, 그 결과를 통해 어떤 부분에서 문제가 발생하는지 배포 전에 확인할 수 있습니다.

**CI 순서**

1. 개발자가 구현한 코드를 기존 코드와 병합 ( 우리의 Mudig의 경우 개발자별 Branch에서 Develop Branch에서 병합 진행, 로컬 테스팅 후 Main에 병합을 진행합니다.)
2. 병합된 코드가 올바르게 동작하고 빌드되는지 검증
3. 테스트 결과 문제가 있다면 다시 1번 과정 진행 , 문제가 없다면 배포

**Github Action을 활용한 CI 구현**

구현 코드

```yml
CI:
  runs-on: ubuntu-latest
  env:
    DJAGNO_SECRET: ${{ secrets.DJAGNO_SECRET }}
  strategy:
    max-parallel: 4
    matrix:
      python-version: ["3.10"]
  steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Tests
      run: |
        python manage.py test
```

##### **지속적인 배포 (Continuous Deployment, CD)**

CD를 간단하게 말하자면, 배포 자동화 과정을 말하며 지속적인 배포를 의미하며,
CI를 통해서 새로운 소스코드의 빌드와 테스트 병합까지 성공적으로 진행됬을 경우 사용자가 사용할 수 있는 배포환경까지 릴리즈 하는 것을 말하고 있습니다.

**CD 순서**

1. CI를 통해 새로운 소스코드의 빌드와 테스트 병합까지 성공
2. 사용자가 사용할 수 있는 배포환경에 릴리즈

**Github Action을 활용한 CD 구현**

구현 코드

```yml
deploy:
  needs: CI
  name: Deploy
  runs-on: ubuntu-latest

  if: success()
  steps:
    - name: executing remote ssh commands using password
      uses: appleboy/ssh-action@master # appleboy를 통해 외부 서버에서 ssh 접속 후 커맨드 실행
      with:
        host: ${{ secrets.AWS_HOST }} # AWS 호스트
        username: ${{ secrets.AWS_USERNAME }} # AWS USERNAME
        key: ${{ secrets.AWS_PEM_KEY }} # AWS PEM KEY
        port: ${{ secrets.AWS_PORT }} # AWS SSH PORT
        script_stop: true
        script: |
          whoami # 현재 내가 로그인한 사용자의 정보를 출력 합니다.
          ls -al # 현재의 디렉토리안의 파일 목록을 출력하여 보여주는 명령어 입니다.
          cd Mudig_BE/ # 뮤딕이 설치된 폴더로 들어갑니다.
          /home/ubuntu/publish/pull_repository.sh # 사전에 정의된 쉘을 실행합니다.
```

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

## 7. 사용자 피드백

2023년 12월 31일부터 2024년 1월 4일까지 총 5일 간 약 40명의 유저분들로 부터 뮤딕이 보안해야할 점과 개선해야할 점 등에 대해서 의견을 받아보았습니다.

적극적으로 테스트에 임해주시고 저희 프로젝트가 발전할 수 있도록 좋은 피드백을 주신 모든분들에게 감사인사를 드립니다!

![스크린샷 2024-01-14 130852](https://github.com/Hyunwooz/programmers/assets/107661525/e9b040b3-3e6c-4bb8-87a4-6bcb68741327)

저희가 사용자 피드백을 받기로 한 목적은 피드백을 수집한다면 우리가 진행중인 프로젝트에서 **어떤 부분이 성공적인지, 개선이 필요한 부분은 어디인지 파악**하는데 도움이 되기 때문이였습니다.

프로젝트를 다양한 시각에서 바라볼 수 있게 해줄 뿐만아니라 사용자 경험적인 부분을 개선하는 데 있어 좋은 효과를 불러올 수 있었습니다.

### 사용자 피드백 수집을 위한 프로세스

#### 1. 사용자 피드백 채널 만들기

저희는 사용자분들의 의견을 쉽게 수집할 수 있도록 Google Forms을 이용하였습니다.

![스크린샷 2024-01-14 130539](https://github.com/Hyunwooz/programmers/assets/107661525/953445ab-8606-491f-ae05-f139cceabf5a)

#### 2. 피드백 분류하기

저희는 아래 이유를 근거로, 표준화된 분류 프로세스를 사용하였습니다.

```
1. 사용자 문제에 대한 응답 시간 단축
2. 문제에 대해 표준화된 우선순위 적용
3. 한정된 자원을 가장 필요하고 영향이 큰 변경 작업에 투입
4. 요청된 작업이 미처리 상태로 계속 남아 있는 것을 방지
```

피드백으로 받은 문제를 아래 3가지 질문에 답하기 위해 구체적인 요구사항을 정의하였습니다.

```
1. 이 문제가 유효한가?
2. 이 문제를 해결할 수 있는가?
3. 이 문제가 얼마나 중요한가?
```

이러한 질문을 통해 조치 가능한 사용자 피드백과 추가 정보가 필요하거나 무시할 수 있는 피드백을 구분하는데 큰 도움이 되었습니다.

**문제가 유효한가?**

좋은 의도를 가지고 피드백을 주셨지만, 우리의 프로젝트와 관련이 없거나 사용자가 설명하는 문제가 이미 해결된 경우가 있기 때문에
사용자 피드백으로 접수된 문제를 평가할 때 '신뢰하되 확인'하는 접근 방식을 취하는게 좋겠다 판단하였습니다.

**문제를 해결할 수 있는가?**

피드백을 적용할 수 있다고 판단했다면 피드백이 조치 가능한지 정하는 것이 다음 순서였습니다.
아래 세가지를 근거로 판단하였습니다.

```
1. 중복되지 않은 지
2. 재현이 가능한 지
3. 범위가 정해져있는 지
```

범위가 너무 크거나 막연한 피드백일 경우 조치를 취할 수 있는 피드백이 아니라 판단하였습니다.

**문제가 얼마나 중요한가?**

마지막으로는 피드백의 조치 우선순위를 정하였습니다. 문제가 얼마나 중요한지, 얼마나 빨리 해결해야 하는지를 근거로 판단하였습니다.
저희의 경우 5단계로 문제를 구분하였습니다.

![스크린샷 2024-01-14 130943](https://github.com/Hyunwooz/programmers/assets/107661525/1bee0e46-7e6c-4ff6-83b9-b4970cd78d0d)

#### 3. 피드백 반영하기

1. 검색 결과 - 음악 찾기 추가

- 플리/유저 검색 뿐만 아니라 음악 검색도 가능하게 되었고, 사용자들은 특정 음악을 검색하여 자신의 플레이리스트에 해당 음악을 쉽게 추가할 수 있게 되었습니다. 이로써 더 다양한 음악 경험과 자신만의 플레이리스트를 만들 수 있는 즐거운 경험을 느낄 수 있게 되었습니다.

2. 음악 생성 결과 7~10개 랜덤으로 변경 , 뮤비 제목 15자 이내로, 설명은 3줄 이내로

- 기존 5개로 고정되어 있던 음악의 수를 최대 10개로 늘리고 7~ 10개 사이로 랜덤 갯수를 부여함으로써 딱딱한 느낌을 벗어나 플레이리스트 생성 경험을 더 다채롭고 생동감 있게 변경하였습니다.

3. 비밀번호 찾기 기능 추가

- 유저들이 비밀번호를 잊어버렸을 때 대비하여, 비밀번호 찾기 기능을 추가하였습니다. 이제 유저들은 자신의 계정에 연결된 이메일 주소를 통해 비밀번호를 복구하고 재설정할 수 있습니다. 이를 통해 유저들이 불편함 없이 계정에 접속할 수 있도록 변경하였습니다.

4. 플레이리스트 썸네일 이미지 변경 추가

- 유저들의 인터렉티브한 경험을 개선하기 위해 생성된 플레이리스트 썸네일을 변경할 수 있는 기능을 추가하였습니다.
