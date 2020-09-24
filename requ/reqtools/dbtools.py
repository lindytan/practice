import pymysql # 要想用pymysql，就必须要导入它



def query(sql):
    # 固定的方法
    # db = pymysql.connect(host='192.144.148.91', user='ljtest', password="Lj123456+", db='ljtestdb')
    db = pymysql.connect(host='118.24.105.78', user='root', password="1qaz!QAZ123***123", db='ljtestdb')
    # 获取查询窗口：游标
    cur = db.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 获取所有的结果
    res = cur.fetchall()
    db.close()
    return res

if __name__ == "__main__":
    # sql = "select * from t_user where username = 'liuyun'"
    sql = "select * from t_user where username = 'python'"
    a = query(sql)
    print(a)

    # 了解一下。
    # u = input("请输入账号：")
    # p = input("请输入密码：")
    # sql = "select * from t_pymysql_account where username='{}' and password='{}'".format(u, p)
    # res = query(sql)
    # if len(res) != 0: # 数据库中寻找到了结果：账号和密码匹配
    #     print("登录成功")
    # else:
    #     print("登录失败")


    # 作业：，请使用python查询商品表t_goods表里面的商品名为 iPhone的价格，并且判断价格如果价格大于5488，则显示买不起，否则显示买买买。

    # 数据库信息：
    # 118.24.105.78
    # root
    # 1qaz!QAZ123***123
    # # 数据库：ljtestdb

    sql = "select * from t_goods where goods='iPhone12'"
    res = query(sql)
    if res[0][2] > 5488:
        print("打扰了，我选华为")
    else:
        print("我爱华为，我选苹果")