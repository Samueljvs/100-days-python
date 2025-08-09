from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

#number_get = driver.find_element(By.XPATH, value = '//*[@id="articlecount"]/ul/li[1]/a', )
#number_get.click()

## Another way is to use link_text

#all_portals = driver.find_element(By.LINK_TEXT, value = "James Costley")
#all_portals.click()

search_button = driver.find_element(By.XPATH, value = '//*[@id="p-search"]/a/span[1]')
search_button.click()

## Get hold of search bar and type into it
search = driver.find_element(By.NAME,  value="search")
search.send_keys("Python", Keys.ENTER)

#driver.quit()