import requests
import pymysql
import pytest
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.exceltools import read_excel
from utils.filetools import read_file,save_file
from utils.filetools import save_filei

def test_01_getinspirer():
    data_res = read_excel("data\接口测试用例.xlsx","inspirer")
    url = data_res[0][2]
    res = requests.get(url=url)
    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_02_inspirernew_success():
    data_res = read_excel("data\接口测试用例.xlsx","inspirer")
    url = data_res[1][2]
    data = eval(data_res[1][4])
    header = eval(data_res[1][5])
    res = requests.post(url=url,json=data,headers=header)
    # print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    iid = res.json()["data"]["inspirerid"]
    save_filei(iid=iid)

def test_03_inspirernew_contentblank_fail():
    data_res = read_excel("data\接口测试用例.xlsx","inspirer")
    url = data_res[2][2]
    data = eval(data_res[2][4])
    header = eval(data_res[2][5])
    res = requests.post(url=url,json=data,headers=header)
    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_04_getuser4status():
    data_res = read_excel("data\接口测试用例.xlsx","inspirer")
    url = data_res[3][2]
    data = eval(data_res[3][4])
    header = eval(data_res[3][5])
    res = requests.post(url=url,json=data,headers=header)
    assert res.status_code == 200
    assert res.json()["status"] == 200
