import pandas as pd 
data = pd.read_excel('data.xlsx',sheet_name="登录")
data["编号"][data["编号"] == 1] =100
data.to_excel("data.xlsx","sheet2")