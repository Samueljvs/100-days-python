import requests
from datetime import datetime as dt

USERNAME = "sammyjohn"
TOKEN = "nskeuh5930274hkjsih4nflk"


pixela_endpoint = "https://pixe.la/v1/users"


pixela_parameters ={
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

## create user
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

## make post request
graph_parameters = {
    "id": "graph1",
    "name": "My Tennis Graph",
    "unit":"Minutes",
    "type":"int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN":TOKEN
}
response = requests.post(url = graph_endpoint, json = graph_parameters, headers=headers)

## Update Graph with a pixel
update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1" E03C-65C0

date_to_use = dt(year = 2025, month = 8, day = 4)

update_graph_config = {
    "date": date_to_use.strftime("%Y%m%d"),
    "quantity":"45"
}

response = requests.post(url = update_graph_endpoint, json = update_graph_config, headers=headers)
print(response)

## PUT will update an existing value

change_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date_to_use.strftime('%Y%m%d')}"
change_data_config = {"quantity":"32"}


response = requests.put(url = change_pixel_endpoint, json =change_data_config,headers=headers)
print(response)