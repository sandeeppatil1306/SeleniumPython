from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/angularpractise")

print(driver.title)

