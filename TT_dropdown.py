from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Chrome()
try:
    driver.get("https://translatelaw.gramener.com/")
    driver.maximize_window()
    driver.find_element(By.ID,"user").send_keys("nidhi.chandra@gramener.com")
    driver.find_element(By.ID,"password").send_keys("0000")
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    time.sleep(2)
    driver.find_element(By.ID,"newprojecModalbtn").click()
    time.sleep(3)
    handles = driver.window_handles
    for h in handles:
        if h != driver.current_window_handle:
            driver.switch_to.window(h)
        break
    driver.find_element(By.XPATH,'//input[@name="projectname"]').send_keys("Automation_Test29")
    ele = driver.find_element(By.XPATH,'//button[@type="submit"]')
    driver.execute_script("arguments[0].scrollIntoView();" ,ele)
    time.sleep(3)
    drop = driver.find_element(By.XPATH,'//select[@id = "assignedUserSelect"]')
    time.sleep(4)
    sel = Select(drop)
    opt = sel.options
    for i in opt:
        
        sel.select_by_visible_text("patriciot tt")
        break
        
    time.sleep(3)
    #driver.save_screenshot("Automat_screenshot.png")


except Exception as e:
    print("Error occurred is ", e)

finally:
    driver.quit()

    
    

