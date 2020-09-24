import requests
import pymysql
import pytest
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file,save_file

"""
def test_00_login():
    url = "http://118.24.105.78:2333/login"
    data = {"username":"tan123","password":"a1234567"}
    res = requests.post(url=url,json=data)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "select * from t_user where username = '{}'".format(data["username"])
    assert len(query(sql)) != 0
    token = res.json()["data"]["token"]
    save_file(token=token)
"""