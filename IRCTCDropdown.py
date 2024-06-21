from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import traceback


driver = webdriver.Chrome()
#driver.implicitly_wait(5)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(15)

try:
    wait = WebDriverWait(driver,10)
    alert = wait.until(EC.alert_is_present())
    
    #alert.dismiss()
    #time.sleep(5)
    print("dismissed successfully")
   
    

except Exception as e :
    print("the error is ", e)
    traceback.print_exc()



