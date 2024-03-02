from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

currentSortedVeggies = []
driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
vegi_Elements = driver.find_elements(By.XPATH,"//tr/td[1]")

for ele in vegi_Elements:
    currentSortedVeggies.append(ele.text)

originalSortedList = currentSortedVeggies.copy()

currentSortedVeggies.sort()

assert currentSortedVeggies == originalSortedList
