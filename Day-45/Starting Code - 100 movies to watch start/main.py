import requests
from bs4 import BeautifulSoup
import re


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL).text
soup = BeautifulSoup(response, 'html.parser')

# get movie lists
movie_titles = soup.find_all(name="h3", class_="title")

title = [title.getText() for title in movie_titles]

split_items = [re.split(r'\)|:', item) for item in title]

new_list = []
counter = 0
for i in split_items:
    split_items[counter][0] = counter+1
    entry = f"{split_items[counter][0]}) {split_items[counter][1]}"
    new_list.append(entry)
    counter +=1

print(new_list)








