from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import time
try:
    class Nykaa:
        def __init__(self):
            self.driver = webdriver.Chrome()
            self.driver.get("chrome://settings/clearBrowserData")
            self.driver.get("https://www.nykaafashion.com/?utm_content=ads&utm_source=GooglePaid&utm_medium=Search&utm_campaign=Search_NykaaFashion&utm_term=Brand_Core&gad_source=1&gclid=CjwKCAjwtqmwBhBVEiwAL-WAYU1Zm5lXOAi-0TdxK4x8jJvajousMzp6dwzRvjC05YIl25zmZpxFXRoCrtQQAvD_BwE")
            self.driver.maximize_window()
            time.sleep(5)
            

        def nykaa(self):
            self.handle = self.driver.current_window_handle
            self.driver.switch_to.window(self.handle)
            self.driver.find_element(By.XPATH,'//button[@id="wzrk-confirm"]').click()
            try:
                WebDriverWait(self.driver,20).until(ec.alert_is_present())
                print("alert found")
                self.al = self.driver.switch_to.alert
                self.al.accept()
                time.sleep(5)

            except T

            

             
            

                #self.al = self.driver.switch_to.alert
                #self.al.dismiss()
            
            
            #except:
                #print("no alert")

            
except:
    print("the error is",ec)

obj = Nykaa()
obj.nykaa()

#def popup(self):
        #self.driver.maximize_window()
        #time.sleep(5)
        #self.dropdown = self.driver.find_element(By.XPATH,"//*[text()='Account']").click()
        #time.sleep(5)
        #self.driver.find_element(By.XPATH,"//button[@class='sub-menu__login ']").click()
      
        #time.sleep(5)
        
        
    
    

        

