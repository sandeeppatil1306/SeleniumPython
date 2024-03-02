import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

service_obj = Service("./chromedriver.exe")
driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

productList = driver.find_elements(By.XPATH, "//div[@class='products']/div")
productCount = len(productList)

assert productCount > 0

for items in productList:
    actualList.append(items.find_element(By.XPATH, "h4").text)
    items.find_element(By.XPATH, "div/button").click()

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[contains(.,'PROCEED TO CHECKOUT')]").click()
# Addition of products price and validate
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)

totalAmt = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totalAmt
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discountedAmt = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert totalAmt > discountedAmt

