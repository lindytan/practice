from dbtools import query
from exceltools import read_excel
import reqtools

res = read_excel("data.xlsx","Sheet1")
print(res[0])
url = res[0][2]
data = eval(res[0][5]) #类型转行
h = eval(res[0][4])  #请求头

res = requests.post(url=url,json=data,headers=headers)
assert res.status_code == 200
assert res.json()["status"] == 200

sql = 
assert len(query(sql)) != 0


