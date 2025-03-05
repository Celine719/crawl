from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


s = Service("E:/download/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome()
driver.get("http://www.dangdang.com/")
driver.implicitly_wait(30)   # 等待时间
input1 = driver.find_element(By.CSS_SELECTOR, ".text.gray")  # 类中的空格用“.”代替
input1.send_keys("爬虫")
search = driver.find_element(By.CSS_SELECTOR, ".button")
search.click()
time.sleep(1)  # 需要等待网页加载，如果没有，会报错，找不到相关元素
name = []
price = []
time.sleep(1)   # 需要时间加载！！！
for i in range(5):
    book_list = driver.find_elements(By.CSS_SELECTOR, " div#search_nature_rg li")  # 记得放循环里，不然一直报错
    # selenium.common.exceptions.StaleElementReferenceException:
    # Message: stale element reference: stale element not found
    for li in book_list:
        name.append(li.find_element(By.CSS_SELECTOR, "a").get_attribute("title"))  # 注意注意！
        price.append(li.find_element(By.CSS_SELECTOR, ".search_now_price").text)
    button = driver.find_element(By.CSS_SELECTOR, "li.next")
    button.click()
print(name)
print(price)
print(len(price))


