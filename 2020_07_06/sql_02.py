"""
pymysql.py读操作
"""
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='',
                     database='stu',
                     charset='utf8')

cur = db.cursor()

sql = "select * from class_1 where class_num = 3;"

cur.execute(sql)
# one_row = cur.fetchone()
# print(one_row)
#
# many_row = cur.fetchmany(2)
# print(many_row)

all_row = cur.fetchall()
print(all_row)

cur.close()
db.close()