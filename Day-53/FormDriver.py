from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
import os

class AutoFill:

    def __init__(self):

        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--lang=en")
        #chrome_options.add_argument(f"--user-data-dir={os.getcwd()}/Day-53/.data")
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        
        
    def populate_form(self, address:list, price:list, link:list):
        for i in range(0, len(address)):
            self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLScncBa-HbdJitYwW2LvMacrVGMuyokkUudBm0YMjg5pmol8tg/viewform?usp=header")
            wait = WebDriverWait(self.driver, 5)
            # answer questions in order
            property_question = wait.until(ec.presence_of_element_located((By.XPATH, 
                                                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
                                                                        ) 
            property_question.send_keys(address[i])

            # Fill in Price
            price_question = wait.until(ec.presence_of_element_located((By.XPATH, 
                                                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
                                                                        )
            price_question.send_keys(price[i])

            # Fill in 
            link_question = wait.until(ec.presence_of_element_located((By.XPATH, 
                                                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
                                                                        )
            link_question.send_keys(link[i])
            # Hit submit
            time.sleep(2)
            sumbit_bttn = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            sumbit_bttn.click()
