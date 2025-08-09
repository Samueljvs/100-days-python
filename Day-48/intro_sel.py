from selenium import webdriver
from selenium.webdriver.common.by import By

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)


#driver.get("https://www.amazon.co.uk/Camping-Backpack-Rucksack-Luggage-Festival/dp/B0B36LYLWN/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.Il4kIvp4rsPde4aZPY5GsHZwaVj-VHN9lszAxN5ASXgf2xy95aB8QW4D-hBLbbYmBm7satgn8oPilKckRYELbDlDCduLwrdsDF75eXs9XsgJ7ixqlBbUBO-YS1D0QDfOemqjY_Vg0L7zhXPtRyAqTaMiYy4n1hxh9Nq33qGdgCo-GoEWqKlMGhMv-g_Nl4z1lbPvu_1ELQksJaB8OXf500K5_maU1URlyAcq2cPJqhmmxcnG81cnt9tIhzLj8KdgrIZEMArqJv3l9jVZM2NqSJcfFE-kiF1WRPd-0P66YyI.TZZqblJjuaULaZ7hfsYOlOq_tVu68XNbQtMb5-H6r3c&dib_tag=se&keywords=Camping%2BRucksacks&qid=1754675260&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

#price_dollar = driver.find_element(By.CLASS_NAME, value = "a-price-whole").text
#price_cents = driver.find_element(By.CLASS_NAME, value = "a-price-fraction").text

#print(f"THe price is {price_dollar}.{price_cents}")

# driver.close() - close a tab
# driver.quit()

## New Challenge - 

driver.get("https://www.python.org/")

## Sam
# text2= driver.find_elements(By.XPATH, value ='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# text_3 = [text.text.split("\n") for text in text2][0]
# dictonary = dict(zip(text_3[0::2], text_3[1::2]))

## ANSWER -- Angle

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget li a")

for time in event_times:
    print(time.text)

for name in event_names:
    print(name.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "event" : event_names[n].text
    }

driver.quit()