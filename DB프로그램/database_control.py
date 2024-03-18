import socket
import sys, os


#HOST = '1.245.214.58'
#PORT = 12345

HOST = '192.168.0.2'
PORT = 12345

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.settimeout(5)

try:
	Socket.connect((HOST,PORT))
	print("connected!!")
except Exception as e:
	print("Connect Fail, retry other HOST IP")
	sys.exit()

def Socket_command(command):
	Socket.send(command.encode())
	reply = Socket.recv(1024)
	print(reply.decode())
	return reply.decode()

def getUser(rfid):
	Socket_command("getUser")
	return Socket_command("select name from paitents where rfid=\""+rfid+"\"")

def upload(rfid,nowDate_time):
	Socket_command("upload")
	# ex) insert into chart valuse('rfid', '2022-04-10 22:10:22', 0,0,0,0)
	return Socket_command("insert into chart values" + "('1111','" + nowDate_time+ "','"+ str(SYS) 
		+"','"+str(DIA)+"','"+str(PUL)+"','"+str(TEM)+"');")

def newuser(msg):
	Socket_command("newuser")
	return Socket_command(msg)

def sql_test(msg):
	Socket_command("command")
	return Socket_command(msg)

msg = "insert into paitents values('2222', '이준호', '남자', 52);"
msg1= "select name from paitents where rfid='10B48A19'"
print(getUser("10B48A19"))
Socket.send("quit".encode())
