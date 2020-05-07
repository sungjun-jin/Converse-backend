## Wecode 7기 1차 프로젝트 Converse Back-end Repository
### 프로젝트 소개
Converse Korea Official Store [컨버스 코리아 공식 스토어](https://www.converse.co.kr/) clone project

### 개발 인원 및 기간
- 기간 : 2020.04.20 - 2020.05.01 (약 2주)
- 개발 인원 : 프론트엔드 [Gwangmin kim](https://github.com/kkm8314), [HeejunShon](https://github.com/HeejunShon), [Seunghyunkim1](https://github.com/Seunghyunkim1) 백엔드 [ensia96](https://github.com/ensia96), [sungjun-jin](https://github.com/sungjun-jin)
- 프론트엔드 [Repository](https://github.com/wecode-bootcamp-korea/Converse-frontend)

### 데모 영상
[![Converse Demo](https://images.velog.io/images/sungjun-jin/post/27aa7f02-baca-4e88-acc3-e9dc1b8fd46d/image.png)](https://www.youtube.com/watch?v=0dYvqMhCsy8&feature=youtube)
---
### 기술
- Python, Django
- Django CORS headers
- Beautifulsoup, Selenium
- Bcrypt, JWT
- MySQL
- Pandas
- AWS EC2, RDS

### 기능
- Beautifulsoup, Selenium Crawler
- 회원가입 / 로그인
- Email, password, birthdate, phone number validation check
- Password encryption with Bcypt
- JSON Web Token을 활용한 access token 발행
- 제품 상세보기
- 사이즈, 색상별 제품 필터링
- 회원별 장바구니 등록 및 목록 가져오기
- 컨버스 매장정보 보기 (with 네이버지도)
- Project deployment with AWS EC2 
- AWS RDS에 DB 세팅 및 EC2 서버 연결

### requirements.txt
```sh
$ pip install -r requirements.txt
```
### API Documentation (with POSTMAN)
Endpoint Documentation [URL](https://documenter.getpostman.com/view/11257941/SzmY9hAR?version=latest#cd32b7e1-449c-4f70-92e8-a0619f242d21)

### ERD (with AQUERY Tool)
AQUERY Tool [URL](https://aquerytool.com:443/aquerymain/index/?rurl=88c304a0-1be6-4e6a-bdf8-4ef49c98dd36)
password : k4payo
![ERD](https://images.velog.io/images/sungjun-jin/post/0b679948-c91c-4fb1-931b-87e79a9b8d66/Converse_ERD.png)
