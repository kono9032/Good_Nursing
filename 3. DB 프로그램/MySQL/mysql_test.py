# -*- coding: utf-8 -*-.
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='capstonedesign', charset='utf8')
cur = conn.cursor()

#cur.execute("create table if not exists patientchart(id char(4), name char(15), sex char(15))")


# cur.execute("insert into paitents values('856590BB', 'Park Gee Hoo','박지후', 'Male', 25);")
# cur.execute("insert into paitents values('10B48A19', 'Gwon Jin hyeok','권진혁', 'Male', 23);")
# cur.execute("insert into paitents values('2222', 'Lee Jun Ho','이준호', 'Male', 52);")
# cur.execute("insert into paitents values('3333', 'Jeon Si Yon','전시윤', 'Female', 17);")
# cur.execute("insert into paitents values('4444', 'Kim Hyun Sik','김현식', 'Male', 35);")
# cur.execute("insert into paitents values('5555', 'Choi Yun Hye','최윤희', 'Female', 47);")
# conn.commit()

cur.execute("insert into chart values('856590BB', '2022-04-10 17:24:03',120, 80, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-04-15 17:24:03',120, 80, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-04-10 01:24:03',120, 80, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-04-10 02:24:03',120, 80, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-04-10 04:24:03',120, 80, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-04-10 06:24:03',120, 80, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-04-10 11:44:03',120, 80, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-04-12 21:14:21',120, 83, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-04-13 13:32:12',120, 84, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-04-14 13:13:32',120, 80, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-04-11 22:23:02',120, 86, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-05-10 22:23:02',120, 86, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-02-10 22:23:02',120, 86, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-09-12 22:23:02',120, 86, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-05-14 22:23:02',120, 86, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-02-17 22:23:02',120, 86, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-09-13 22:23:02',120, 86, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-10-10 22:23:02',120, 86, 70, 36.5);")
cur.execute("insert into chart values('856590BB', '2022-11-17 22:23:02',120, 86, 70, 36.5);")
cur.execute("insert into chart values('10B48A19', '2022-09-10 01:23:01',120, 80, 70, 36.5);")
cur.execute("insert into chart values('10B48A19', '2022-06-17 07:44:42',120, 80, 70, 36.5);")
cur.execute("insert into chart values('10B48A19', '2022-05-14 12:23:13',120, 80, 70, 36.5);")
cur.execute("insert into chart values('10B48A19', '2022-02-10 10:14:32',120, 80, 70, 36.5);")
cur.execute("insert into chart values('10B48A19', '2022-04-10 11:23:13',120, 80, 70, 36.5);")
cur.execute("insert into chart values('2222', '2022-04-10 17:24:03',120, 80, 70, 36.5);")
conn.commit()

# rfid = '1111'
# text = "insert into chart values" + "(" + rfid+ ", '2022-04-10 17:24:03', 0, 0, 0, 0);"
# cur.execute(text)
# conn.commit()


# cur.execute("select * from paitents")
# cur.execute("delete from chart;")
# conn.commit()


#cur.execute("select * from paitents where rfid='2222';")
result = cur.fetchall()
print(result)
conn.close()