from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()

# Load cookies from a browser session
driver.get("https://www.makemytrip.com/")  
driver.maximize_window()

wins = driver.window_handles
for i in wins:
    if i != driver.current_window_handle:
        driver.switch_to.window(i)

wait = WebDriverWait(driver, 20)
fr = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="webklipper-publisher-widget-container-notification-close-div"]')))


fr.click()


#popup = driver.find_element(By.XPATH, '//section[@data-cy="CommonModal_2"]')


#wait.until(ec.frame_to_be_available_and_switch_to_it, popup)

# Now you can interact with the main content of the page
# For example, clicking on the dropdown and selecting a country

# Find and click on the dropdown button
#dropdown_button = driver.find_element(By.XPATH, '//*[@id="SW"]/div[1]/div[2]/div[2]/div/section/form/div[1]/div/div')
#dropdown_button.click()

# Wait for the dropdown options to appear
#time.sleep(5)  # Adjust the wait time as needed

# Select the desired country from the dropdown
# select = Select(dropdown_button)
# select.select_by_visible_text("United States")

# Wait for a while (for demonstration purposes)
time.sleep(5)

# Close the browser
driver.quit()
