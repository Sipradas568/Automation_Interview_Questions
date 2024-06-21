from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import pygetwindow as gw
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
    main = driver.current_window_handle
    wins = driver.window_handles
    for i in wins:
            if i != main:
                    driver.switch_to.window(i)
            break
    driver.find_element(By.XPATH,'//input[@name="projectname"]').send_keys("Automation_Test29")
    ele = driver.find_element(By.XPATH,'//button[@type="submit"]')
    driver.execute_script("arguments[0].scrollIntoView();", ele)
    driver.find_element(By.XPATH,'//input[@type="file"]').send_keys("C:\\Users\\sipra.das\\Documents\\TTT_Sample Documenets\\Long story in English with moral Two (2) - Copy.pdf")
    
    time.sleep(5)
    add_files_button = driver.find_element(By.XPATH,'//button[@id="addFiles"]')
    add_files_button.click()

    file_dialog = gw.getActiveWindow()

# Activate the file dialog window
    file_dialog.activate()
    time.sleep(4)

# Use keyboard shortcuts to set the file path
    pyautogui.write(r"C:\Users\sipra.das\Documents\TTT_Sample Documenets\_pdf_storage_espanol-texto-barcelonah.pdf")
    time.sleep(3)
    pyautogui.press("Enter") 
  
    time.sleep(4)
    ele.click()
    time.sleep(3) 
    driver.refresh()
    time.sleep(3) 

except Exception as e:
       print("error ocurred",e)

finally:
       driver.quit()

