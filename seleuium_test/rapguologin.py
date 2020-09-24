import time
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()  # 让浏览器最大化
driver.get("http://118.24.105.78:9000/shopxo/admin.php")

# step1:手动的输入账号密码，去登录成功然后获取登录之后的cookie
# time.sleep(20)
# print(driver.get_cookies()) # 获取cookie

# step2:使用登录之后的cookie去访问网页，就能绕过登录
driver.delete_all_cookies() 
cookie = {'domain': '118.24.105.78', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': '6e0riqrhg2qvcbihsinkl7f1i2'}
driver.add_cookie(cookie)

driver.refresh()