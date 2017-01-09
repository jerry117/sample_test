from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# 使用键盘操作全选 剪切 粘贴功能
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('教育')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL,'a')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL,'x')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL,'v')
driver.find_element_by_xpath('//*[@id="su"]').send_keys(Keys.ENTER)
time.sleep(5)
driver.close()