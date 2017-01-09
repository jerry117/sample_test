# coding:utf-8
from selenium import webdriver
from time import sleep

# 设置chrome显示大小
Nexus4 = {
    "deviceMetrics":{"width":360,"height":640,"pixelRatio":2},
    "userAgent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36"
}
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("mobileEmulation",Nexus4)
driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.get("http://www.XXX.com")
sleep(3)
driver.find_element_by_link_text("测试").click()
sleep(4)
# 使用js脚本运行
js = "var c=document.querySelector(\'.v-mask\');c.click()"
driver.execute_script(js)
sleep(4)
driver.close()
