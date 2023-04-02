from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path="C:\development\chromedriver.exe"
options = webdriver.ChromeOptions()
driver=webdriver.Chrome(service=Service(chrome_driver_path),options=options)

def browser_function():
    driver.get("https://python.org")
   
    event_times=driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
    event_names=driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
   
    events={}
    for n in range(len(event_times)):
        events[n]={
            "time":event_times[n].text,
            "name":event_names[n].text
        }
    print(events)
   
 
browser_function()