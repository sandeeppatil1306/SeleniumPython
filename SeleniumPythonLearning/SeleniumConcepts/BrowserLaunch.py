from selenium import webdriver


from selenium.webdriver.chrome.service import Service

service_obj = Service("./chromedriver.exe")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
title = driver.title
print(driver.current_url)
print(title)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.back()
driver.refresh()
driver.forward()

