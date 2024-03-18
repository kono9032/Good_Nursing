#-*- encoding: utf8 -*-
#bind error ---> netstat -nao | findstr "포트번호"
#taskkill /f /pid 3624
from flask import Flask, render_template, request, url_for, redirect, session
from datetime import timedelta
# import pymysql

app = Flask(__name__)
app.secret_key = 'sdf9032/@#@rfv@#5'
# app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=1)

@app.route('/login/login.cgi')
def cgi():
	return redirect(url_for('login'))

@app.route('/')
@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/<msg>')
def login_msg(msg):
	return render_template('login.html', alarm=msg)

@app.route('/join')
def join():
  return render_template('join.html')

@app.route('/home')
def home():
	print(session)
	if(not('user' in session)):
		return redirect(url_for('login'))
	# conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='capstonedesign', charset='utf8')
	# cur = conn.cursor()
	# cur.execute("select * from paitents")
	# q = cur.fetchall()
	# conn.close()
	return render_template('main.html', list1=q)

@app.route('/chart/<RFID>')
def chart(RFID):
	if(not('user' in session)):
		return redirect(url_for('login'))
	# conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='capstonedesign', charset='utf8')
	# cur = conn.cursor()
	# cur.execute("select * from paitents")
	# q = cur.fetchall()
	# cur.execute("select ko_name from paitents where rfid='"+ RFID +"';")
	# name = cur.fetchall()[0][0]
	# cur.execute("select * from chart where rfid='"+ RFID +"'order by date_time DESC;")
	# p = cur.fetchall()
	# conn.close()
	return render_template('main.html', list1=q, list2=p, name = name + '씨의 검사 기록입니다')

@app.route('/loading', methods =['POST', 'GET'])
def loading():
	if request.method == 'POST':
		rfid = request.form['RFID']
		return redirect(url_for('chart', RFID = rfid))
	else:
		return redirect(url_for('home'))

@app.route('/login_confirm', methods=['POST'])
def login_confirm():
	id_ = request.form['id_']
	pw_ = request.form['pw_']
	# conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='capstonedesign', charset='utf8')
	# cur = conn.cursor()
	# cur.execute("select pw from user where id='"+id_+"';")
	# value = cur.fetchall()
	# conn.close()
	if(len(value)):
		if(value[0][0] == pw_):
			session['user'] = id_
			return redirect(url_for('home'))

		else:
			return redirect(url_for('login_msg', msg="wrong_pw"))
	else:
		return redirect(url_for('login_msg', msg ="wrong_id"))

@app.route('/create_id', methods=['POST'])
def create_id():
	id_ = request.form['id_']
	pw_ = request.form['pw_']
	# conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='capstonedesign', charset='utf8')
	# cur = conn.cursor()
	# print("insert into user values('"+id_+"','"+pw_+"');")
	# cur.execute("insert ignore into user values('"+id_+"','"+pw_+"');")
	# conn.commit()
	# conn.close()
	return redirect(url_for('login'))

if __name__ == "__main__":
  app.run(debug=True,host="0.0.0.0", port=8080)