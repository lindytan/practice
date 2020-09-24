from selenium import webdriver
import time

#1,打开浏览器
driver = webdriver.Chrome(executable_path='chromedriver.exe')

#2，输入网址
driver.get("http://www.baidu.com/")

#3，操作元素
e = driver.find_element_by_id("kw")
e.send_keys("自动化测试")
driver.find_element_by_id("//*[@id="su"]").click()

time.sleep(5)
i = driver.title
print(i)