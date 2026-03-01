from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://the-internet.herokuapp.com/login")

# -------- Positive Test Case --------
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

if "secure" in driver.current_url:
    print("Positive Test Passed")
else:
    print("Positive Test Failed")

driver.get("https://the-internet.herokuapp.com/login")

# -------- Negative Test Case --------
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

if "invalid" in driver.page_source:
    print("Negative Test Passed")
else:
    print("Negative Test Failed")
input("Press Enter to close browser...")
driver.quit()