"""
pymysql.py
增删改操作
"""
import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user='root',
                     password='',
                     database='stu',
                     charset='utf8')

cur = db.cursor()

name = str(input("name:"))
age = int(input("age:"))
sex = str(input("gender('w','m'):"))
score = float(input("score:"))
class_num = int(input("class_num:"))

# 第一种方法
# sql = "insert into class_1(name,age,sex,score,class_num) values ('%s',%d,'%s',%f,%d)" % (name, age, sex, score, class_num)
# cur.execute(sql)

# 第二种方法
try:
    sql = "insert into class_1(name,age,sex,score,class_num) values (%s,%s,%s,%s,%s);"
    cur.execute(sql, [name, age, sex, score, class_num])

    # 修改操作
    sql1 = "update class_1 set age=45 where name='诸葛亮';"
    cur.execute(sql1)

    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭数据库
cur.close()
db.close()
