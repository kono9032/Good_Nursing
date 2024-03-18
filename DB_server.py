#-*- encoding: utf-8 -*-. - 
#bind error ---> netstat -nao | findstr "포트번호"
#taskkill /f /pid 3624
import socket
import pymysql
import sys, os

HOST = '192.168.35.144'
PORT = 12345


# HOST = '1.245.214.58'
# PORT = 12345


db_conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='capstonedesign', charset='utf8')
db_cur = db_conn.cursor()

(soc, conn, addr) = None, None, None

class comunicateProgram():
	def make_list(self,result):
		send_str = ""
		for i in range(1,len(result[0])):
			send_str = send_str + str(result[0][i])+","
		return send_str[0:-1]

	def __init__(self, parent=None):
		while True:
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
				soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				print("socket created")
				#soc.settimeout(None)
				soc.bind((HOST,PORT))
				soc.listen(1)
				print ('Socket awaiting messages')
				(conn, addr) = soc.accept()
				print ('Connected :', conn,addr)
				while True:
					try:
						data = conn.recv(1024).decode()
						print ('From client------- : ' + data)

						if data == 'getUser':
							conn.send("Ready...".encode())
							rfid = conn.recv(1024).decode()
							print(rfid)
							db_cur.execute("select * from paitents where rfid=\'"+rfid+"\'")
							result = db_cur.fetchall()
							if(len(result) != 0):
								conn.send(self.make_list(result).encode())
							else:
								db_cur.execute("select * from paitents where rfid='999999'")
								result = db_cur.fetchall()
								conn.send(self.make_list(result).encode())

						elif data == 'upload':
							conn.send("Ready...".encode())
							data = conn.recv(1024).decode()
							print(data)
							try:
								db_cur.execute(data)
							except:
								conn.send("Fail.".encode())
								continue
							db_conn.commit()
							conn.send("success!".encode())


						elif data == 'quit':
							conn.send('Terminate'.encode())
							conn.close()
							soc.close()
							break

						else:
							reply = 'Unknown command'
							conn.send(reply.encode())
							print("To client--------- : ", reply)
							print("\n")
						
					except KeyboardInterrupt:
						conn.close()
						soc.close()
						sys.exit()

					except Exception as e:
						# 연결 종료 등 에러가 발생할 시 다시 소켓을 생성하기 위함
						exc_type, exc_obj, exc_tb = sys.exc_info()
						fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
						print(e, exc_type, fname, exc_tb.tb_lineno)
						conn.close()
						soc.close()
						break

if __name__ == '__main__':
	cp = comunicateProgram()