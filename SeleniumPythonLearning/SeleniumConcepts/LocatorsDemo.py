from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("./chromedriver.exe")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Sandeep")
driver.find_element(By.NAME, "email").send_keys("sandeep1@yopmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
submitMessage = driver.find_element(By.CLASS_NAME, "alert-success").text
print(submitMessage)
assert "Success" in submitMessage

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("ddsd")
