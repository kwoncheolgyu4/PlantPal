# PlantPal
PlantPal은 Spring boot와 python으로 개발된 식물 분류 웹 프로젝트입니다
## 프로젝트 개요
이 분류 웹은 식물을 이미지화시켜 업로드 및 분류를 실행하면 식물의 이름을 알려주는 목적으로 제작되었습니다. 주요 기능은 다음과 같습니다
- 이미지를 업로드 후 실행 버튼을 누르면 식물 명을 알림
- 카카오 맵에 식물 분포도를 표시하여 알림
## 버전 히스토리
### Version 1
- 식물 데이터를 수집 및 전처리
- tensorflow의 keras를 통하여 분석 모델 생성
- Spring boot와 python의 화면 합치기
- 산림청 식물 분포도 csv를 활용하여 카카오맵에 마커 표시
### Version 2
- 내부 와이파이 망을 통하여 핸드폰 접속이 가능하도록 ip 및 권한 설정
## 기술 스택
### Front-End
- HTML / CSS / Javascript
- BootStrap
### Back-End
- Spring boot
- java
- python
## 소스 참고
- 수업내용 참고
## Spring boot Version
- 3.3.5
## 주의사항
- 이 프로젝트를 실행하기 위해서는 AIHUB의 동의보감 독초판별 이미지 데이터와 산림청 식물분포도 csv가 필요합니다.
