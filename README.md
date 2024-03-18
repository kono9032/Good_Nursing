# Good_Nursing
간호사의 업무 부담을 줄여주는 결합형 체온-혈압계
- 주요 내용 : 체온계와 혈압계가 결합된 구조로 휴대가 편리한 Iot 의료기기
- 주요 업무 : HW, SW 제작 일체
- 기술 스택 : Arduino, RaspberryPI, HTML, SoildWorks, C, python, Mysql
- 업무 기간 : 2021.12~2022.10 (약 10개월)
- 개발 인원 : 2명


## 파일 설명
1. 체온계
    - 플랫폼 : Arduino 
    - 사용 언어 : C
    - 주요 동작 : RFID 리더, 온도 측정, 혈압계와 Bluetooth 통신<br>
                 OLED 표시, 동작 단계별 진동 모터 구동 (햅틱 기능)

2. 혈압계
    - 플랫폼 : RaspberryPI
    - 사용 언어 : python
	- 주요 라이브러리 : pyqt5
    - 주요 동작 :<br>
        (1) GUI 표시 / 혈압, 체온, 환자 정보<br>
        (2) 체온계로 부터 RFID ID, 체온 값 수신<br>
        (3) RFID ID를 key value로 DB에서 환자 정보 조회<br>
        (4) 혈압, 체온, 측정 시간 값 조회한 환자 DB에 저장

3. DB 프로그램
	- 플랫폼 : RaspberryPI, Mysql
	- 사용 언어 : python, SQL
	- 주요 라이브러리 : socket
	- 주요 동작 : 단말기(혈압계)로 부터 수신한 명령에 따라 DB제어<br>
		(1) 조회 : RFID ID를 key value로 환자정보 조회<br>
		(2) 저장 : 측정 값 저장<br>
		(3) 종료 : socket close<br>

4. 웹페이지
	- 플랫폼 : RaspberryPI
	- 사용 언어 : python, html, css, js
	- 주요 동작 : DB 조회, 이름 검색, 로그인, 회원가입
