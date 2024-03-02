from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

'''
Headless Mode
'''
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")

#service_obj = Service()

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

driver.get_screenshot_as_file("screenshot2.png")
