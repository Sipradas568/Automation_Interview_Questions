from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://www.nykaafashion.com/?utm_content=ads&utm_source=GooglePaid&utm_medium=Search&utm_campaign=Search_NykaaFashion&utm_term=Brand_Core&gad_source=1&gclid=CjwKCAjwtqmwBhBVEiwAL-WAYU1Zm5lXOAi-0TdxK4x8jJvajousMzp6dwzRvjC05YIl25zmZpxFXRoCrtQQAvD_BwE")
driver.maximize_window()
time.sleep(6)

driver.find_element(By.XPATH,"//button[@id='wzrk-cancel']").click()
act = ActionChains(driver)
el = driver.find_element(By.XPATH ,"//span[text() = 'More']")
act.move_to_element(el).perform()
time.sleep(4)
ele1 = driver.find_element(By.XPATH ,"//img[@src='https://adn-static1.nykaa.com/nykdesignstudio-images/pub/media/wysiwyg/mm_images/Sale/Luxe.jpg?rand=1711970988&']")
ele1.click()
time.sleep(5)






