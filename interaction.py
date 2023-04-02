from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path="C:\development\chromedriver.exe"
options = webdriver.ChromeOptions()
driver=webdriver.Chrome(service=Service(chrome_driver_path),options=options)

def browser_function():
    driver.get("http://orteil.dashnet.org/experiments/cookie/")
    cookie=driver.find_element(By.XPATH,'//*[@id="cookie"]')
    
    
    while True:
        cookie.click()
        # time.sleep(5)
        

browser_function()
   