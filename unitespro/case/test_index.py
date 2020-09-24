"""
首页的模块测试用例相关
"""

import unittest
from selenium import webdriver
import time

class TestCaseIndex(unittest.TestCase):
    #成员方法(类里面的方法),每个方法表示一个测试用例
    def test_01_search(self):
        driver = webdriver.Chrome(executable_path='driver\chromedriver.exe')
        driver.get("https://www.baidu.com/")
        driver.maximize_window()
        driver.find_element_by_id('kw').send_keys("")
        driver.find_element_by_id('su').click()
        driver.implicitly_wait()
#调试
if __name__ == "__main__":
    unittest.main()