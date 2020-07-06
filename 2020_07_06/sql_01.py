"""
pymysql.py
"""
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost", port=3306, user="root",
                     password="", database="stu", charset="utf8")

cur = db.cursor()

sql = "insert into class_1(name,age,sex,score,class_num) values ('zhangshan',20,'m',99,3),('lisi',22,'m',45,3);"

# 执行sql语句
cur.execute(sql)

db.commit()

cur.close()
db.close()