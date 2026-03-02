from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open Login Page
driver.get("https://the-internet.herokuapp.com/login")

# ----------------------------
# ✅ Test Case 1: Valid Login
# ----------------------------
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

if "secure" in driver.current_url:
    print("Test Case 1 Passed: Valid Login Successful")
else:
    print("Test Case 1 Failed")

driver.get("https://the-internet.herokuapp.com/login")

# ----------------------------
# ❌ Test Case 2: Invalid Login
# ----------------------------
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

if "Your username is invalid!" in driver.page_source:
    print("Test Case 2 Passed: Invalid Login Detected")
else:
    print("Test Case 2 Failed")

driver.get("https://the-internet.herokuapp.com/login")

# ----------------------------
# ❌ Test Case 3: Empty Fields
# ----------------------------
driver.find_element(By.ID, "username").send_keys("")
driver.find_element(By.ID, "password").send_keys("")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

if "Your username is invalid!" in driver.page_source:
    print("Test Case 3 Passed: Empty Fields Validation Working")
else:
    print("Test Case 3 Failed")

# Close Browser
input("Press Enter to close browser...")
driver.quit()
