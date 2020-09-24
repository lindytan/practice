import requests
import pymysql
import pytest
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.exceltools import read_excel
from utils.filetools import read_file,save_file
from utils.filetools import read_filei

def test_01_getinspirerr():
    data_res = read_excel("data\接口测试用例.xlsx","inspirerdetails")
    url = data_res[0][2]
    res = requests.get(url=url)
    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_02_getcomments():
    data_res = read_excel("data\接口测试用例.xlsx","inspirerdetails")
    url = data_res[1][2]
    data = eval(data_res[1][4])
    header = eval(data_res[1][5])
    res = requests.post(url=url,json=data,headers=header)
    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_03_getuser4status():
    data_res = read_excel("data\接口测试用例.xlsx","inspirerdetails")
    url = data_res[2][2]
    data = eval(data_res[2][4])
    header = eval(data_res[2][5])
    res = requests.post(url=url,json=data,headers=header)
    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_04_usercollections():
    data_res = read_excel("data\接口测试用例.xlsx","inspirerdetails")
    url = data_res[3][2]
    data = eval(data_res[3][4])
    header = eval(data_res[3][5])
    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    

def test_05_userfellgoods():
    data_res = read_excel("data\接口测试用例.xlsx","inspirerdetails")
    url = data_res[4][2]
    data = eval(data_res[4][4])
    header = eval(data_res[4][5])
    res = requests.post(url=url,json=data,headers=header)
    assert res.status_code == 200
    assert res.json()["status"] == 200


def test_06_commentnew():
    data_res = read_excel("data\接口测试用例.xlsx","inspirerdetails")
    url = data_res[5][2]
    data = eval(data_res[5][4])
    header = eval(data_res[5][5])
    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_07_commentupdate():
    data_res = read_excel("data\接口测试用例.xlsx","inspirerdetails")
    url = data_res[6][2]
    data = eval(data_res[6][4])
    header = eval(data_res[6][5])
    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_08_commentdelete():
    data_res = read_excel("data\接口测试用例.xlsx","inspirerdetails")
    url = data_res[7][2]
    data = eval(data_res[7][4])
    header = eval(data_res[7][5])
    res = requests.post(url=url,json=data,headers=header)
    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_09_inspirerdelete():
    data_res = read_excel("data\接口测试用例.xlsx","inspirerdetails")
    url = data_res[8][2]
    data = eval(data_res[8][4])
    header = eval(data_res[8][5])
    res = requests.post(url=url,json=data,headers=header)
    assert res.status_code == 200
    assert res.json()["status"] == 200
