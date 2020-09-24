import requests
import pymysql
import pytest
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.exceltools import read_excel
from utils.filetools import save_file


def test_01_get_title_img():
    data_res = read_excel("data\接口测试用例.xlsx","index")
    url = data_res[0][2]
    header = eval(data_res[0][5])
    res = requests.get(url=url,headers=header)
    # print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "select count(*) from `ljtestdb`.`t_title_img`"#where 'status'=1 
    # for i in res.json()["data"]:
    #     if len(i) == query(sql):
    #         print("测试通过！")
    #     else:
    #         return("测试失败",len(i),query(sql))

def test_02_getcoures():
    data_res = read_excel("data\接口测试用例.xlsx","index")
    url = data_res[1][2]
    res = requests.get(url=url)
    # print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] ==200
    sql = "SELECT * FROM `ljtestdb`.`t_coures` where 'status'= 2;"
    # for i in res.json()["data"]:
    #     if len(i) == query(sql):
    #         print("【{}】测试通过".format(data_res[1][1]))
    #     else:
    #         print("【{}】测试失败".format(data_res[1][1]))

def test_03_getquestions():
    data_res = read_excel("data\接口测试用例.xlsx","index")
    url = data_res[2][2]
    res = requests.get(url)
    # print(res.txt)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    #  for i in res.json()["data"]["id"]:
    #     sql = "SELECT * FROM `ljtestdb`.`t_questions` where 'id' = {}".format(i))
    #     if i == len(query(sql)):
    #         print("【{}】测试通过".format(data_res[2][1]))
    #     else:
    #         print("【{}】测试失败".format(data_res[2][1]))

def test_04_getarticle():
    data_res = read_excel("data\接口测试用例.xlsx","index")
    url = data_res[3][2]
    res = requests.get(url=url)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    # print(res.text)
    # for i in res.json()["data"]["id"]:
    #     sql = "SELECT * FROM `ljtestdb`.`t_article` where 'id' = {}".format(i))
    #     if i == query(sql):
    #         print("【{}】测试通过".format(data_res[3][1]))
    #     else:
    #          print("【{}】测试失败".format(data_res[3][1]))

def test_05_getinspirer():
    data_res = read_excel("data\接口测试用例.xlsx","index")
    url = data_res[4][2]
    res = requests.get(url=url)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    # print(res.text)
    # sql = "SELECT * FROM `ljtestdb`.`t_inspirer` where 'status' = 1"
    # for i in res.json()["data"]:
    #     if len(i) == query(sql):
    #         print("【{}】测试通过".format(data_res[4][1]))
    #     else:
    #         print("【{}】测试失败".format(data_res[4][1]))

def test_06_gethighusers():
    data_res = read_excel("data\接口测试用例.xlsx","index")
    url = data_res[5][2]
    res = requests.get(url=url)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    # print(res.text)
    # sql = "SELECT * FROM `ljtestdb`.`t_` where 'status' = 1"
    # for i in res.json()["data"]:
    #     if len(i) == query(sql):
    #         print("【{}】测试通过".format(data_res[5][1]))
    #     else:
    #         print(("【{}】测试失败".format(data_res[5][1])))


