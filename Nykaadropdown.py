from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select 
import time
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
pop = driver.find_element(By.XPATH,'//section[@data-cy = "CommonModal_2"]')
try:
    wins = driver.window_handles
    for i in wins:
        if i == pop:
            driver.switch_to.window(i)
        break

    time.sleep(8)
    ele = driver.find_element(By.XPATH ,'//i[@class = "drop-down down"]')
    ele.click()

    select = Select(ele)
    select.select_by_visible_text("United States")
    time.sleep(6)

except:
    print(EC)

