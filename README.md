# Good_Nursing
간호사의 업무 부담을 줄여주는 결합형 체온-혈압계
- 주요 내용 : 체온계와 혈압계가 결합된 구조로 휴대가 편리한 Iot 의료기기
- 주요 업무 : HW, SW 제작 일체
- 기술 스택 : Arduino, RaspberryPI, HTML, SoildWorks, C, python, Mysql
- 업무 기간 : 2021.12~2022.10 (약 10개월)
- 개발 인원 : 2명

파일 설명

1. 체온계
    - 플랫폼 : Arduino 
    - 사용 언어 : C
    - 주요 동작 : RFID 리더, 온도 측정, 혈압계와 Bluetooth 통신
                 OLED 표시, 동작 단계별 진동 모터 구동 (햅틱 기능)

2. 혈압계
    - 플랫폼 : RaspberryPI
    - 사용 언어 : python
    - 주요 동작 :
        (1) GUI 표시 / 혈압, 체온, 환자 정보
        (2) 체온계로 부터 RFID ID, 체온 값 수신
        (3) RFID ID를 key value로 DB에서 환자 정보 조회
        (4) 혈압, 체온, 측정 시간 값 조회한 환자 DB에 저장