
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


driver.maximize_window()

wait = WebDriverWait(driver,5)
act_res = []
lst = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
wait.until(EC.presence_of_element_located((By.XPATH,'//input[@placeholder="Search for Vegetables and Fruits"]'))).send_keys("ber")
results = driver.find_elements(By.XPATH,'//h4[contains(text(),"ber")]')
for res in results:
    act_res.append(res.text)
    print(act_res)


assert lst == act_res

    
    
   
    



