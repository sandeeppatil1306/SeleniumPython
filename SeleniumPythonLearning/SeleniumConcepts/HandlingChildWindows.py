from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("./chromedriver.exe")
driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
openWindowsList = driver.window_handles

driver.switch_to.window(openWindowsList[1])
pageText = driver.find_element(By.TAG_NAME,"h3").text
print(pageText)
driver.close()
driver.switch_to.window(openWindowsList[0])
print(driver.find_element(By.TAG_NAME,"h3").text)
