from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

driver_path = '/Users/jerryli/Downloads/chromedriver'

driver = webdriver.Chrome(driver_path)
url = "https://www.baidu.com"
driver.get(url)

# 下拉框
# mouse = driver.find_element("link text", "设置")
# ActionChains(driver).move_to_element(mouse).perform()
# time.sleep(0.5)
# driver.find_element("link text", "搜索设置").click()
# time.sleep(1)

# 方法一：直接定位
# 选择下拉框选项的第三项
# driver.find_element_by_xpath(".//*[@id='nr']/option[3]").click()
# 若此时点击后，下拉选项未收回，可点击整个下拉框，收回下拉选项
# driver.find_element_by_xpath(".//*[@id='nr']").click()


# 方法二：二次定位
# 第一步：定位下拉框
# parent = driver.find_element_by_id("nr")
# 第二步：在下拉框中，定位子元素，并操作
# parent.find_element_by_xpath('.//option[@value="20"]').click()


# select用法

# 先定位到下拉框
# s = driver.find_element_by_id("nr")


# 第一种：根据索引定位（从0开始）
# Select(s).select_by_index(0)
# 收回下拉选项
# s.click()


# 第二种：根据value属性定位
# 如：value = 50
# Select(s).select_by_value("50")
# 收回下拉选项
# s.click()


# 第三种：根据选项内容定位
# Select(s).select_by_visible_text("每页显示20条")
# 收回下拉选项
# s.click()




# driver.close()