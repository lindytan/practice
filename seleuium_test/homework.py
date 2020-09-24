from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
# driver.get("http://118.24.105.78:8080/ljindex/")
driver.maximize_window()
# 注册
# driver.find_element_by_link_text("注册").click()
# time.sleep(5)
# driver.find_element_by_id("username").send_keys("tan111")
# driver.find_element_by_id("phonenum").send_keys("18222222223")
# driver.find_element_by_id("password").send_keys("a1234567")
# driver.find_element_by_id("confirpw").send_keys("a1234567")
# driver.find_element_by_id("emailnum").send_keys("937588911@qq.com")
# driver.find_element_by_id("userRegist").click()
#登录
driver.get("http://118.24.105.78:8080/ljindex/index.html")
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("tan111")
driver.find_element_by_id("password").send_keys("a1234567")
driver.find_element_by_id("userLogin").click()
#点赞
time.sleep(15)
driver.find_element_by_xpath('//*[@id="xdth"]/li[1]/div/div[1]').click()
driver.find_element_by_xpath('//*[@id="user_likes"]').click()
a = driver.find_element_by_id("experience_likes")
assert a.text == "1"
#评论
driver.find_element_by_id("experience_comments_ctt").send_keys("评论点东西")
driver.find_element_by_id("experience_comments_btn").click()
b = driver.find_element_by_xpath("//*[@id='comment']/div/div[2]/div/div/div[1]/p[1]")
assert b.text == "用户399523"
# driver.quit()

