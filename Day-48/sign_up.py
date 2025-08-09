from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

## Set up driver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

# FIRST NAME
fname = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
fname.send_keys("Sam")
#LAST NAME
lname = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
lname.send_keys("JV")
#Email
email = driver.find_element(By.XPATH, value='/html/body/form/input[3]')
email.send_keys("akehefh@gmail.com")

# signup
sign_up = driver.find_element(By.XPATH, value='/html/body/form/button')
sign_up.click()