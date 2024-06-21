from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
drop = driver.find_element(By.CSS_SELECTOR,"#dropdown-class-example")
sel = Select(drop)

time.sleep(5)
for i in sel.options:
    sel.select_by_value("option3")

time.sleep(5)