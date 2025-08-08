import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/2000-08-12"

header = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

response = requests.get(url = URL, headers= header)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
song_container = soup.find_all(name="div", class_="o-chart-results-list-row-container")

song_container = [songs.find("h3").getText().strip() for songs in song_container]
 
