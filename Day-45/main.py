from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

#process for one
art = soup.find(name="span", class_="titleline")
upvote = soup.find(name='span', class_='score')

link_tag = art.find("a")

article_title = art.get_text()
aritcle_link = link_tag.get('href')
article_upvote = upvote.get_text()

#process for all
article = soup.find_all(name="span", class_="titleline")

title_list = [title.get_text() for title in article]
href_list = [href.find('a').get('href') for href in article]
up_vote_list = [int(votes.get_text().split()[0]) for votes in soup.find_all(name='span', class_='score')]



print(title_list[up_vote_list.index(max(up_vote_list))])
print(href_list[up_vote_list.index(max(up_vote_list))])









#article_link = ""
#article_upvote ""


# for sub in subs:
#     print(sub.get_text())

# with open("Day-45/website.html") as website:
#    data = website.read()

# soup = BeautifulSoup(data, 'html.parser')

# print(soup.prettify())
# print(soup.title.string)
# all_anchor_tags = soup.find_all(name='a')

# for tag in all_anchor_tags:
#    print(tag.get_text())
#    print(tag.get('href'))
# # get tag name by element and id, can also be done by class
# heading = soup.find(name='h1', id='name')
# print(heading.get_text())

# print(soup.find(name='h3', class_='heading'))

