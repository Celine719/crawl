from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

s = Service("./chromedriver.exe")
driver = webdriver.Chrome(options=options)
# 发送请求
driver.get("http://www.baidu.com/")
kw = driver.find_element(By.ID, "kw")
kw.send_keys("爬虫")
driver.find_element(By.CSS_SELECTOR, "#su").click()  # 点击
# 点击按钮
# su = driver.find_element(By.CSS_SELECTOR, "#su") “.”表示class
# su.click()

# 网页出现广告一样，利用爬虫获取按钮


# 例子：翻译


