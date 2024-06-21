from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH,'//div[@class="products"]/div[1]/div[2]/a[2]').click()
driver.find_element(By.XPATH,'//div[@class="products"]/div[1]/div[2]/a[2]').click()
driver.find_element(By.XPATH,'//div[@class="products"]/div[1]/div[3]').click()
driver.find_element(By.XPATH,'//img[@alt="Cart"]').click()
time.sleep(3)
pop= driver.find_element(By.XPATH,'//div[@class="cart-preview active"]')
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located,pop)
pop.find_element(By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]').click()
time.sleep(3)
qty = driver.find_element(By.XPATH, '//table[@class="cartTable"]/tbody/tr/td[3]/p')
q = qty.text
assert q == '3' 
print(q)
time.sleep(3)
