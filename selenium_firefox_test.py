import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('http://www.lamian.tv/search/video?keyword=')
        # self.assertIn("Python",driver.title)
        elem = driver.find_element_by_id("skeyword")
        elem.send_keys("pycon")
        elem1 = driver.find_element_by_class_name("search-btn1")
        elem1.click()
        sleep(5)
        driver.refresh()
        elem = driver.find_element_by_id("skeyword")
        elem.send_keys("")
        elem1 = driver.find_element_by_class_name("search-btn1")
        elem1.click()
        sleep(5)
        elem = driver.find_element_by_id("skeyword")
        elem.send_keys("pycon1")
        elem1 = driver.find_element_by_class_name("search-btn1")
        elem1.click()
        # assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
