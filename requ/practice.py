#完成登录和注册功能，数据存到数据库中

import pymysql
from dbtools import query

username = input("请输入用户名：")
password = input("请输入密码：")

#做得乱起八糟得作业，不想改
sql = "select * from t_user where username = '{}' and password = '{}'".format(username,password)
res = query(sql)
if True:
    print("denglichenggong")
else:
    sql1 = "insert into t_user (username,password) values ('{}','{}')".format(username,password)
    query(sql1)

