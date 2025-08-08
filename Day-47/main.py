import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib

#load env variables and parameters
load_dotenv(dotenv_path="Day-47/.env") 
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en;q=0.9",
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}

EMAIL = 'Sammy.Verevis@gmail.com'
PASSWORD = os.getenv("EMAIL_PASSWORD")

COMPARE_PRICE = float(100.00)

## Scrape website
response = requests.get(url = URL, headers=headers)
response.raise_for_status()

response_text = response.text
soup = BeautifulSoup(response_text, 'html.parser')

print(soup.prettify())

# Get Price
soup_price = soup.find(name="span", class_="a-price aok-align-center")

print(soup_price)
price= float(soup_price.getText().split(sep="$")[1])

## Get Title
item_name = soup.find(name="span", class_="a-size-large product-title-word-break").getText()
new_text = str(" ".join(item_name.split()).encode('utf-8').strip())

print(item_name)
print(new_text)


#Print the email if price drops below 99.99
if price < COMPARE_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user = EMAIL, password = PASSWORD )
        connection.sendmail(
            from_addr = EMAIL, 
            to_addrs = 'Sam.John.Vs@gmail.com', 
            msg = f"Subject:Item Price Drop\n\n The {new_text} price has dropped below ${price}, buy now! \n {URL}"
            )