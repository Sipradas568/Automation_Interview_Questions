from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/flights/")
driver.maximize_window()
time.sleep(2)
handles = driver.window_handles
for h in handles:
        if h != driver.current_window_handle:
            driver.switch_to.window(h)
        break

wait = WebDriverWait(driver,10)

contain = wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class = "imageSlideContainer"]')))
contain.find_element(By.XPATH,'//span[@class = "commonModal__close"]').click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,'input[id="fromCity"]').send_keys("Mald")
time.sleep(3)
lists = driver.find_elements(By.XPATH ,'//ul[@role="listbox"] /li[2]/div/div/p/span[1]')
for li in lists:
    if li.text == "Villa Airport" :
        li.click()
    break
time.sleep(2)
opt = driver.find_element(By.ID,'fromCity')
assert opt.get_attribute("value") == "Maamigili islan..."

    


