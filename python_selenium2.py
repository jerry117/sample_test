
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# by的用法
# driver.find_element("id", "kw")
# driver.find_element(By.ID, "kw")

driver_path = '/Users/jerryli/Downloads/chromedriver'

class Base():
    '''基于原生的selenium做二次封装'''
    def __init__(self, driver:webdriver.Chrome) -> None:
        self.driver = driver
        self.timeout = 10
        self.t = 0.5
        
    def find(self, locator, value=''):
        '''定位到元素， 返回元素对象，没定位到， timeout异常 locator 传元组。如（'id', 'kw'）'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id", "values")')
        else:
            print()



