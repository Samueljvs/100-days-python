from bs4 import BeautifulSoup
import requests
import FormDriver

#----------------------- 1. Get soup ------------------------------#
URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url = URL)
zillow_pg = response.text
soup = BeautifulSoup(zillow_pg, "html.parser")

#----------------------- 2. Get information ------------------------------#
cards = soup.find_all(name='li', class_='ListItem-c11n-8-84-3-StyledListCardWrapper')

link = [card.find('a').get('href') for card in cards]
address = [card.find('address').getText().strip() for card in cards]
price = [card.find(name = 'span', class_="PropertyCardWrapper__StyledPriceLine").getText() for card in cards]

#----------------------- 3. Populate template------------------------------#

bot = FormDriver.AutoFill()

bot.populate_form(address, price, link)

