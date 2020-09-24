import unittest
from selenium import webdriver
from utils.seleniumtools import find_element


#unittest 的测试用例是以类来管理的
class TestCaseIndex(unittest.TestCase):
    def test_01_baobao(Self):
        #seleunim的code
        driver = webdriver.Chrome(executable_path='driver\\chromedriver.exe')
        driver.maximize_window()
        driver.get("http://118.24.255.132:9090/shopxo/")
        baobao = ("xpath",'//*[@id="floor1"]/div[2]/div[2]/div[1]/div/div/a')
        e = find_element(driver,baobao)
        assert e.text == "MARNI Trunk 女士 中号拼色十字纹小牛皮 斜挎风琴包"
