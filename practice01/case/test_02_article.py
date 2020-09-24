import requests
import pymysql
import pytest
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.exceltools import read_excel
from utils.filetools import read_file,save_file


def test_01_getmytaglist():
    data_res = read_excel("data\接口测试用例.xlsx","article")
    url = data_res[0][2]
    header = eval(data_res[0][5])
    res = requests.get(url=url,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    #数据库查验
def test_02_newmytag_3failed():
    data_res = read_excel("data\接口测试用例.xlsx","article")
    url = data_res[1][2]
    data = eval(data_res[1][4])
    header = eval(data_res[1][5])
    res = requests.post(url=url,json=data,headers=header)
    # print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_03_newmytag_7failed():
    data_res = read_excel("data\接口测试用例.xlsx","article")
    url = data_res[2][2]
    data = eval(data_res[2][4])
    header = eval(data_res[2][5])
    res = requests.post(url=url,headers=header,json=data)
    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_04_newmytag_5success():
    data_res = read_excel("data\接口测试用例.xlsx","article")
    url = data_res[3][2]
    data = eval(data_res[3][4])
    header = eval(data_res[3][5])
    res = requests.post(url=url,headers=header,json=data)
    assert res.status_code == 200
    assert res.json()["status"] == 200


def test_05_articlenew_success():
    data_res = read_excel("data\接口测试用例.xlsx","article")
    url = data_res[4][2]
    data = eval(data_res[4][4])
    header = eval(data_res[4][5])
    res = requests.post(url=url,headers=header,json=data)
    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_06_articlenew_titleblank():
    data_res = read_excel("data\接口测试用例.xlsx","article")
    url = data_res[5][2]
    data = eval(data_res[5][4])
    header = eval(data_res[5][5])
    res = requests.post(url=url,headers=header,json=data)
    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_07_articlenew_contentblank():
    data_res = read_excel("data\接口测试用例.xlsx","article")
    url = data_res[6][2]
    data = eval(data_res[6][4])
    header = eval(data_res[6][5])
    res = requests.post(url=url,headers=header,json=data)
    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_08_articlenew_briefblank():
    data_res = read_excel("data\接口测试用例.xlsx","article")
    url = data_res[7][2]
    data = eval(data_res[7][4])
    header = eval(data_res[7][5])
    res = requests.post(url=url,headers=header,json=data)
    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_09_articlenew_tagsblank():
    data_res = read_excel("data\接口测试用例.xlsx","article")
    url = data_res[8][2]
    data = eval(data_res[8][4])
    header = eval(data_res[8][5])
    res = requests.post(url=url,headers=header,json=data)
    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_10_articlenew_tokenblank():
    data_res = read_excel("data\接口测试用例.xlsx","article")
    url = data_res[9][2]
    data = eval(data_res[9][4])
    header = eval(data_res[9][5])
    res = requests.post(url=url,headers=header,json=data)
    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_11_articlenew_wrongtoken():
    data_res = read_excel("data\接口测试用例.xlsx","article")
    url = data_res[10][2]
    data = eval(data_res[10][4])
    header = eval(data_res[10][5])
    res = requests.post(url=url,headers=header,json=data)
    assert res.status_code == 200
    assert res.json()["status"] == 401