import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("./chromedriver.exe")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
time.sleep(5)

radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
for radioButton in radiobuttons:
    radioButton.click()

time.sleep(5)

assert driver.find_element(By.ID,"displayed-text").is_displayed()

driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()