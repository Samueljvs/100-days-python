from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
from dotenv import load_dotenv
from datetime import datetime as dt

# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------

# Create Chrome Profile and create account manually. Put YOUR email and password here:
ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
# Keep the browser open if the script finishes or crashes.
# If True, you need to *manually* QUIT Chrome before you re-run the script.
chrome_options.add_experimental_option("detach", True)
# Create a folder for the Chrome Profile Selenium will use every time
user_data_dir = os.path.join(os.getcwd(), "Day-49/profile_path")
# include double -- for command line argument to Chrome
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

# Navigate to site
driver.get(GYM_URL)

# ----------------  Step 2 - Automated Login ----------------

# Alternative to using time.sleep(): use a standalone wait object
wait = WebDriverWait(driver, 2)

# Click login button to go to login page
login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_btn.click()

# Fill in login form
email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID, "password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

# Click Login
submit_btn = driver.find_element(By.ID, "submit-button")
submit_btn.click()

# Wait for schedule page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# Getting a SessionNotCreatedException?
# Remember to *Quit* Selenium's Chrome Instance before trying to click "run"

# ----------------  Step 3 - Book A Class tuesday 6pm ----------------

# Get the cards and parse date and time
WEEKDAY_SLOT = 1
TIME_SLOT = 18

booking_cards = driver.find_elements(By.CLASS_NAME, value='ClassCard_card__KpCx5')

for class_check in booking_cards:
    text = class_check.find_element(By.CLASS_NAME, value="ClassCard_cardActions__tVZBm").text
    class_name = class_check.find_element(By.CSS_SELECTOR, "h3").text
    if text == 'Booked':
        print(f"Already Booked in for {class_name}")
    elif text == "Waitlisted":
        print(f"Already waitlisted for {class_name}")
    elif text == 'Join Waitlist':
       class_check.find_element(By.CLASS_NAME, value="ClassCard_cardActions__tVZBm").click()

# class_id = [booking.get_attribute('data-class-id') for booking in booking_cards] ## Get list

# # Get all the dates and times of the bookings
# class_date_time =[]

# for date in class_id:
#     parts = date.split(sep="-")
#     date = dt.strptime(f"{parts[3]}-{parts[2]}-{parts[1]} {parts[4][:2]}:{parts[4][2:]}", "%d-%m-%Y %H:%M")
#     class_date_time.append(date)

# # Book for Tuesday weekday == 1 and time also == 1800

# for i in range(0, len(class_date_time)):
#     if dt.weekday(class_date_time[i]) == WEEKDAY_SLOT and class_date_time[i].hour == TIME_SLOT:
#         card_to_book = booking_cards[i]
#         book = card_to_book.find_element(By.CLASS_NAME, value="ClassCard_cardActions__tVZBm")
#         book.click()

#driver.quit()



