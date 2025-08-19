from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
import os


class InternetSpeedTwitterBot:

    def __init__(self):  
        self.up = 0
        self.down = 0
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--lang=en")
        chrome_options.add_argument(f"--user-data-dir={os.getcwd()}/Day-53/.data")
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        # reject cookies
        try:       
            reject_bttn = self.driver.find_element(By.CSS_SELECTOR, "#onetrust-reject-all-handler")
            reject_bttn.click()
            print("cookies rejected")
        except NoSuchElementException:
            print("No cookie popup found, continuing...")
        # Continue with Test

        go_bttn = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_bttn .click()
        print("Running Speed Test")

        time.sleep(60)

        up_speed = self.driver.find_element(By.XPATH, 
                                                '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        down_speed = self.driver.find_element(By.XPATH, 
                                                  '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        self.up = up_speed
        self.down = down_speed

        print(f"Download speed was: {self.down}")
        print(f"Upload speed was: {self.up}")

        self.driver.quit()

# -----------Note I need to make this bottom to work properly ----------- #
    def tweet_at_provider(self, email:str, password:str):
        self.driver.get("https://x.com/settings/account?lang=en")

        time.sleep(5)
        # login process
        login_bttn = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
        login_bttn.click()    

        time.sleep(5)

        sign_in_bar = self.driver.find_element(By.XPATH, 
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        sign_in_bar.clear()
        sign_in_bar.send_keys(email)
        sign_in_bttn = self.driver.find_element(By.XPATH, 
                                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        sign_in_bttn.click()

        time.sleep(5)

        pass_bar = self.driver.find_element(By.XPATH, 
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_bar.clear()
        pass_bar.send_keys(password)

        login_bttn2 = self.driver.find_element(By.XPATH, 
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login_bttn2.click()

        time.sleep(10)
        print("I'm in!")

        