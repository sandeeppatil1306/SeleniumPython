import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("./chromedriver.exe")
driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

time.sleep(2)
productList = driver.find_elements(By.XPATH, "//div[@class='products']/div")
productCount = len(productList)

assert productCount > 0

for items in productList:
    items.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[contains(.,'PROCEED TO CHECKOUT')]").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

promoConfirmation = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(promoConfirmation)
