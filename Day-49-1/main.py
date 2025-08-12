from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import os
from dotenv import load_dotenv
from datetime import datetime as dt
import time

load_dotenv(dotenv_path="Day-49-1/.env")  # Manually load .env

email = os.getenv("LINKED_EMAIL")
password = os.getenv("LINKED_PASS")

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=4279991526&f_AL=true&geoId=100992797&keywords=data%20scientist&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'

chrome_options = webdriver.ChromeOptions()
# Keep the browser open if the script finishes or crashes.
# If True, you need to *manually* QUIT Chrome before you re-run the script.
chrome_options.add_experimental_option("detach", True)
# Create a folder for the Chrome Profile Selenium will use every time
user_data_dir = os.path.join(os.getcwd(), "Day-49-1/profile_path")
# include double -- for command line argument to Chrome
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to site
driver.get(URL)

# Reject popup
time.sleep(2)
reject_popup = driver.find_element(By.XPATH, '//*[@id="close-small"]')
reject_popup.click()

## Click sign-in
sign_in = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/form/p/button')
sign_in.click()

time.sleep(5)

email_input = driver.find_element(By.NAME, value='session_key')
email_input.send_keys(email)

pass_input = driver.find_element(By.NAME, value='session_password')
pass_input.send_keys(password)

login = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/form/div[2]/button')
login.click()

# wait = WebDriverWait(driver, 5)  # wait up to 5 seconds for elements

# locators = [
#     (By.XPATH, '/html/body/div[1]/header/nByav/div/a[2]'),
#     (By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/form/div[2]/button'),
#     (By.XPATH, '//*[@id="main-content"]/div[1]/form/p/button')
# ]

# clicked = False
# for by, path in locators:
#     try:
#         btn = wait.until(ec.presence_of_element_located((by, path)))
#         btn.click()
#         print(f"Clicked sign-in button: {path}")
#         clicked = True
#         break
#     except TimeoutException:
#         continue

# if not clicked:
#     print("No sign-in button found.")

# ------------------------ Get list of jobs and apply for the first one ------------------------ ##


time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value='.jobs-save-button')
apply_button.click()