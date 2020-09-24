from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.taobao.com/")
diver.maximize_window()
driver.find_element_by_id('q').send_keys("海南之家")
driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
driver.title

driver.quit()