# -*- coding: utf-8 -*-
import sys, os
import threading
import datetime
import socket
from dock_ver3 import *
from controlView_ui import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QDateTime, QDate, Qt, QBasicTimer
from time import sleep
from random import *
from bluetooth import*

import serial, time
import psycopg2

import RPi.GPIO as GPIO


font = "font: 12pt \"Open Sans\";\n""gridline-color: rgb(0, 0, 0);\n""color:rgb(225, 126, 66);\n""background:transparent;"
code,code2,message = "","",""
User_Data = ["0","","","","","","","","","","",""] # User_Data[en_name, ko_name, en_sex, ko_sex, age]

PUL = 0 #pulse 맥박 / 60~100회
DIA = 0 #diastolic b.p 이완기 혈압 / 60~80
SYS = 0 #systolic b.p 수축기 혈압 / 90~120
TEM = 0 #bodytemprature 체온
BT_flag = True # 블루투스 장치 연결 여부 

Motor_PIN = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor_PIN, GPIO.OUT, initial=GPIO.LOW)

# ---------------------------------------------------------------------------
# ----------------------------- 혈압측정기 serial ----------------------------
# ---------------------------------------------------------------------------

#Serial port / bloodpressure data
SERIALPORT="/dev/ttyAMA0"
BAUDRATE = 19200

sr = serial.Serial(SERIALPORT, BAUDRATE)
conn = None
cur = None
bloodData = None
lastData = ["BLOODPRESSURE","0","0","0"]
isFirst = True
isDone = False
#timeout 0은 동작 안함
sr.timeout = 0.1

def Serial_Connection():
	try:
		if sr.isOpen() == True :
			print("Already opened the serial port.")
		else :
			sr.open()
			print("Success opened the serial port.")

		
		sr.flushInput()
		sr.flushOutput()
		time.sleep(0.1)

	except Exception as e : 
		print("Exception: Opening serial port: " + str(e))

def blood_pressure(self, ui):
	global PUL,SYS,DIA, isFirst, isDone
	print("blood pressure.")
	sr.flushInput()
	sr.flushOutput()
	time.sleep(0.1)
	isFirst = True
	while True: 
		try:
			response = sr.readline()
			if response :
				print(response)
			# 수신데이터가 b'BLOODPRESSURE,138,86,68\r' 이렇게 들어오기 때문에 데이터 파싱이 필요함.
			# 앞뒤 불필요 문자 제거.
			response = str(response).replace("b'", "").replace("'", "")

			
			if response.startswith('BLOODPRESSURE'):
				# \r 개행문자가 replace로 치환이 되지 않아 끝에 두 문자 별도로 제거
				# 최종 데이터 BLOODPRESSURE,138,86,68 
				rcvData = response[:-2]			
				print(f"blood: {rcvData}")
				bloodData = rcvData.split(",")
				lastData = rcvData.split(",")

				# 측정이 완료되는 시점(backup 데이터와 현재 수신받은 데이터가 다른경우 측청 행위로 판단.)
				if bloodData[1] != lastData[1] and bloodData[2] != lastData[2] and bloodData[3] != lastData[3] :
					
					# 새롭게 축정한 데이터 백업
					lastData[1] = bloodData[1]
					lastData[2] = bloodData[2]
					lastData[3] = bloodData[3]
					
					# 최초 부팅시 continue
					if isFirst == True:
						isFirst = False
					else:
						PUL = bloodData[3]
						SYS = bloodData[1]
						DIA = bloodData[2]
						isDone = True
						print("Measuring complete.")
						
						ui.uiUpdateDelegate.emit(1)
					

		except Exception as e:
			print(f"Error communicating: {str(e)}")

# ---------------------------------------------------------------------------
# ------------------------ 데이터 베이스 통신 영역 ----------------------------
# ---------------------------------------------------------------------------
def Database_Connection():
	try:
		global conn, cur, bloodData
		conn = None
		cur = None
		bloodData = None
		conn = psycopg2.connect(
			host = 'stackhigh-db.ceaeypme4kcd.ap-northeast-2.rds.amazonaws.com', 
			user = 'tester', 
			password = 'tester12#$',
			dbname='stackhighdb', 
			port=5432
			)
		cur = conn.cursor()
		print("Success connect to database.")
	except Exception as e : 
		print(f"Exception: Connect to database: {str(e)}")

def InsertVitalSignData(time):
	try:
		#						   맥박, 수축, 확장
		global User_Data, message, PUL, SYS, DIA, TEM, isFirst, isDone, newcode
		cur = conn.cursor()
		cur.execute(
			"""
			insert into testdb.vitalsignmaster 
			(emr_reg_num, measure_datetime, sbp_value, dbt_value, pr_value, bt_value, rr_value) 
			values 
			(%s, %s, %s, %s, %s, %s, %s) ;
			"""
			,(User_Data[1], str(time), SYS, DIA, PUL, TEM, "")
		)
		conn.commit()
		print("Information was successfully inserted.")
	except (Exception, psycopg2.Error) as e:
		print(f"insert error: {e}")
	

def SelectPatient(rfid):
	try:
		print("select user")
		
		cur = conn.cursor()
		cur.execute("select emr_reg_num, patient_name, gender, emr_bir_dte, emr_rrn, emr_phone_num, emr_address, emr_insure_info, emr_gudian_name, emr_gudian_phn_num, emr_gudian_relation from testdb.patientinfo where emr_reg_num = %s", [rfid])

		User_Data[0] = str(cur.rowcount)
		if cur.rowcount > 0 :
			rows = cur.fetchall()
			i = 0
			for dt in rows[0]:
				i = i + 1
				User_Data[i] = dt
		
		print("Successfully selected information.")
		for index, value in enumerate(User_Data):
			print(index, value)

		return User_Data
	except (Exception, psycopg2.Error) as e:
		print(f"select error: {e}")
		User_Data[0] = "2"

		return User_Data


def SaveData():
	global User_Data, message, PUL, SYS, DIA, TEM, isFirst, isDone, newcode, font
	global code2, code
	
	nowDate_time = "0000-00-00 00:00:00"
	dt = datetime.datetime.now()
	nowDate_time = dt.strftime('%Y-%m-%d %H:%M:%S')          


	if isDone == True and TEM != 0:			
		InsertVitalSignData(nowDate_time)
		font = "font: 12pt \"Open Sans\";\n""color: rgb(225, 126, 66);\n""gridline-color: rgb(0, 0, 0);\n""background:transparent;"
		message = "저장이 완료되었습니다"
		thread = threading.Thread(target=message_delay, args=(None,ui))
		thread.daemon = True
		thread.start()
		isDone = False
		PUL = 0
		DIA = 0
		SYS = 0
		TEM = 0
	else:
		User_Data = SelectPatient(code)
		font = "font: 14pt \"Open Sans\";\n""color: rgb(255, 0, 0);\n""gridline-color: rgb(0, 0, 0);\n""background:transparent;"
		message = "측정을 완료해 주십시요"
		thread = threading.Thread(target=message_delay2, args=(None,ui))
		thread.daemon = True
		thread.start()
# ---------------------------------------------------------------------------
# --------------------- 메시지 깜박임 효과 영역 -------------------------------
# ---------------------------------------------------------------------------
def message_delay(self, ui):
	global message
	ui.uiUpdateDelegate.emit(1)
	sleep(3)
	message = ""
	ui.uiUpdateDelegate.emit(1)

def message_delay2(self, ui):
	global message
	tmp = message
	for i in range(0,3):
		sleep(0.05)
		message = ""
		ui.uiUpdateDelegate.emit(1)
		sleep(0.05)
		message = tmp
		ui.uiUpdateDelegate.emit(1)

	sleep(2)
	message = ""
	ui.uiUpdateDelegate.emit(1)

# ---------------------------------------------------------------------------
# ------------------- 체온계 블루투스 통신 영역 -------------------------------
# ---------------------------------------------------------------------------

def bluetooth(self,ui):
	global font,client_socket,PUL,SYS,DIA,TEM,BT_flag,User_Data,code,code2,hello
	global message, newcode
	newcode = ""
	nowDate_time = "0000-00-00 00:00:00"
	while True:
		ui.uiUpdateDelegate.emit(1)
		if (BT_flag != False): # bluetooth device is available, status = True
			client_socket=BluetoothSocket( RFCOMM )
			BT_flag = client_socket.connect_ex(("98:da:60:01:a4:b2",1)) #original 98:da:60:01:a4:b2 / 98:DA:60:01:A7:BE
			print("waiting...")
			# print(BT_flag)
			sleep(1.5)
		else:
			try:
				raw_recv_data = str(client_socket.recv(1024))
				recv_data = ""
				print(raw_recv_data)
				if(len(raw_recv_data)>0):
					for i in range(0, len(raw_recv_data), 1):
						recv_data = recv_data + raw_recv_data[i]
						if(raw_recv_data[i] == "Z"):
							newcode = recv_data
							recv_data = ""
				print(newcode)
				if newcode.find("BT") != -1:   
					TEM = round(float(newcode[newcode.index("BT")+2:-1]),1)
					newcode = ""
					dt = datetime.datetime.now()
					nowDate_time = dt.strftime('%Y-%m-%d %H:%M:%S')                   
					print(nowDate_time)

				if newcode.find("BC") != -1:
					if(conn != None):
						code = newcode[newcode.index("BC")+2:-1]
						User_Data = SelectPatient(code)
						message = ""
						if User_Data[0] == "0" :
							font = "font: 14pt \"Open Sans\";\n""color: rgb(255, 0, 0);\n""gridline-color: rgb(0, 0, 0);\n""background:transparent;"
							message = "등록되지 않은 환자입니다 :<"
							code = ""
							code2 = ""
							User_Data = ["0","","","","","","","","","","",""]
							thread = threading.Thread(target=message_delay2, args=(None,ui))
							thread.daemon = True
							thread.start()
						elif User_Data[0] == "2" :
							font = "font: 14pt \"Open Sans\";\n""color: rgb(255, 0, 0);\n""gridline-color: rgb(0, 0, 0);\n""background:transparent;"
							message = "정보를 불러오는데 실패하였습니다 :<"
							code = ""
							code2 = ""
							User_Data = ["0","","","","","","","","","","",""]
							thread = threading.Thread(target=message_delay2, args=(None,ui))
							thread.daemon = True
							thread.start()
						else:
							font = "font: 12pt \"Open Sans\";\n""color: rgb(225, 126, 66);\n""gridline-color: rgb(0, 0, 0);\n""background:transparent;"
					else:
						font = "font: 14pt \"Open Sans\";\n""color: rgb(255, 0, 0);\n""gridline-color: rgb(0, 0, 0);\n""background:transparent;"
						message = "서버연결이 필요합니다"
						thread = threading.Thread(target=message_delay2, args=(None,ui))
						thread.daemon = True
						thread.start()

			except Exception as e:
				print(e)
				BT_flag = True

				continue
		ui.uiUpdateDelegate.emit(1)

# ---------------------------------------------------------------------------
# ------------------ 그래픽 유저 인터페이스 영역 ------------------------------
# ---------------------------------------------------------------------------
class controlView(QtWidgets.QDialog, Ui_Dialog):
	def __init__(self):
		super(controlView,self).__init__()
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.pushButton_clicked)
		self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
		self.pushButton_3.clicked.connect(self.pushButton_3_clicked)
		self.pushButton_4.clicked.connect(self.pushButton_4_clicked)
		self.pushButton_5.clicked.connect(self.pushButton_5_clicked)
		s  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		ip = s.getsockname()[0]
		print(s.getsockname()[0])
		self.local_ip.setText(ip)
		self.show()

	def pushButton_clicked(self):
		if conn != None:
			conn.close()
		pid = os.getpid()
		os.kill(pid, 2) 
		#쓰레드에서 프로그램을 종료할때 사용.

	def pushButton_2_clicked (self):
		if conn != None:
			conn.close()
		os.system("sudo reboot")
		sys.exit(app.exec_())

	def pushButton_3_clicked (self):
		self.close()

	def pushButton_4_clicked (self):
		try:
			Database_Connection()
			print("connected!!")
			self.status_label.setText("connected!!")
		except Exception as e:
			print("Connect Fail, retry other HOST IP")
			self.status_label.setText("Fail")

	def pushButton_5_clicked (self):
		global DIA, SYS, PUL, TEM, User_Data
		DIA = 0
		SYS = 0
		PUL = 0
		TEM = 0
		User_Data = ["0","","","","","","","","","","",""] 
		self.status_label.setText("Cleared")


class MyFirstGuiProgram(QtWidgets.QMainWindow, Ui_MainWindow):
	global code2,code,font
	uiUpdateDelegate = pyqtSignal(int)
	
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent=parent)
		self.date = QDate.currentDate()
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.changeTime)
		self.timer.start(1000) # 1초 timer start
		self.setupUi(self)
		self.uiUpdateDelegate.connect(self.uiUpdater)
		self.function_button.clicked.connect(self.function_button_clicked)
		self.start_button.clicked.connect(self.start_button_clicked)
		self.start_button.pressed.connect(self.start_button_pressed)
		self.start_button.released.connect(self.start_button_released)
		self.save_button.clicked.connect(self.save_button_clicked)
		self.progressValue(0)

		self.uiUpdateDelegate.emit(1)

	def changeTime(self):
		self.datetime = QDateTime.currentDateTime()
		self.date_now.setText(self.datetime.toString("yyyy년 MM월 dd일  a hh:mm"))
		
	def uiUpdater(self,MainWindow):
		global message
		self.message.setStyleSheet(font)
		self.TEM.setText(str(TEM))
		self.PUL.setText(str(PUL))
		self.DIA.setText(str(DIA))
		self.SYS.setText(str(SYS))
		self.number.setText(code)
		self.name.setText(User_Data[1])
		self.sex.setText(User_Data[2])
		self.age.setText(User_Data[3])
		self.message.setText(message)
		if (BT_flag != False):
			self.bt_device.setStyleSheet("background:transparent;\n" "border:none;")
			self.bt_state.setText("disconnected")
		else:
			self.bt_device.setStyleSheet("background-image: url(:/newPrefix/bt_device.png);\n" "border:none;")
			self.bt_state.setText("Thermometer is ready")

	def function_button_clicked(self):
		self.controlView_widget = controlView()
		self.controlView_widget.exec_()
		self.uiUpdateDelegate.emit(1)

	def start_button_pressed(self):
		self.graphicsView.setStyleSheet("background-image: url(:/newPrefix/main_pushed.PNG);")
		GPIO.output(Motor_PIN, 1)
		time.sleep(0.05)
		GPIO.output(Motor_PIN, 0)

	def start_button_released(self):
		self.graphicsView.setStyleSheet("background-image: url(:/newPrefix/main_released.PNG);")
		


# ---------------------------------------------------------------------------
# ---------------------------- 혈압계 구동 영역 ------------------------------
# ---------------------------------------------------------------------------	

	def save_button_clicked(self):
		SaveData()

	def start_button_clicked (self):
		self.timer = QBasicTimer()
		self.step = 0
		print("start_button_clicked")
		self.timer.start(50, self)
		self.start_button.setDisabled(True)

	def timerEvent(self, e): # 혈압계 측정 영역
		global PUL, SYS, DIA, isDone
		settime = 8
		self.step = self.step + 1
		if self.step >= settime*20:
			self.progressValue(self.step/settime*5)
			self.timer.stop()
			self.start_button.setEnabled(True)
			PUL = randint(60, 100)
			SYS = randint(110, 130)
			DIA = randint(70, 80)
			self.uiUpdateDelegate.emit(1)
			GPIO.output(Motor_PIN, 1)
			time.sleep(0.05)
			GPIO.output(Motor_PIN, 0)
			print("end")
			isDone = True
			return
		self.progressValue(self.step/settime*5)
		
	
	def progressValue(self,value): #혈압계 게이지 효과
		StyleSheet = """
		QFrame{
		background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} 
		rgba(255, 90, 90, 187), stop:{STOP_2} rgba(255, 255, 255, 0)); border-radius: 108px}
		"""
		progress = (100 - value) / 100.0
		if(progress>0): 
			stop_2 = str(progress - 0.001)
		else:
			stop_2 = str(progress)
		stop_1 = str(progress)

		newStylesheet = StyleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
		self.frame.setStyleSheet(newStylesheet)

if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)
	ui = MyFirstGuiProgram()
	# ui.show()
	ui.showFullScreen()
	Serial_Connection()
	Database_Connection()
	thread = threading.Thread(target=bluetooth, args=(None,ui))
	thread.daemon = True
	thread.start()
	bloodThrad = threading.Thread(target=blood_pressure, args=(None,ui) )
	bloodThrad.daemon =True
	bloodThrad.start()

	sys.exit(app.exec_())