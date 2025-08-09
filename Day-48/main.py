from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

## Click language
english = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
english.click()


## Sleep again for page load
sleep(3)

bigCookie = driver.find_element(By.ID, value='bigCookie')  # Get all cookies

item_ids = [f"product{i}" for i in range(18)] ## get all product items


## SET play timer

start_time = time()
last_action_time = time()

while True:
    bigCookie.click()

    current_time = time()

    if current_time - last_action_time >= 5:  ## this is not right
        for product in item_ids:
            item = driver.find_element(By.ID, value=product)
            item.click()
        
        last_action_time = current_time

    
    if time() - start_time > 300 :
        driver.quit()
        
            