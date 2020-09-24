import requests
from dbtools import query

"""
url = "http://192.144.148.91:2333/get_title_img"
res = requests.get(url)
print(res.json()["status"])
print(res.status_code)
assert res.status_code == 200
assert res.json()["status"] == 200

#数据库校验,
#查询所有轮播图id是否都存在

data = res.json()["data"]

for i in data:
    # print(i["id"]) 
    # print(i[0]) # 字典取值不能用下标，要用key
    sql = "select * from t_title_img where id = {}".format(i["id"])
    res = query(sql)
    assert len(res) != 0
    """
#post类型
url1 = "http://192.144.148.91:2333/login"
headers = {"Content-Type":"application/json"}
data ={"username":"tan123","password":"a1234567"}
res1 = requests.post(url=url1,headers=headers,json=data)
token = res1.json()["data"]["token"]

url2 = "http://192.144.148.91:2333/inspirer/new"
headers2 = {"Content-Type":"application/json","token":token}
data2 = {"content":"内容"}
res2 = requests.request(url=url2,headers=headers2,json=data)
print(res2.text)
