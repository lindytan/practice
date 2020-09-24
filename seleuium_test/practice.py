from selenium import webdriver
from seleniumtools import find_element

# driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://www.baidu.com")
# driver.find_element_by_id("mq").send_keys("包包")
# driver.find_element_by_xpath("/form/fieldset/div/button").click()


# driver.quit()

e = ("id",'kw')
r = ("id",'su')
find_element(driver,e).send_keys("自动化测试")
find_element(driver,r).click()

