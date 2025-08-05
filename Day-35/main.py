# import package
import os
import requests
from twilio.rest import Client
from datetime import datetime as dt

month = dt.datetime.now().month, 
day = dt.datetime.now().day

print(month)
print(day)

api_key = "xx"

account_sid = ["xx"]
auth_token = ["xx"]


MY_LAT = 39.933365
MY_LNG = 32.859741

# Set parameters to get 5 day weather forecast
parameters = {"q": "Ankara", 
              "appid": api_key,
              "cnt":4}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params= parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for i in weather_data:
   condition = weather_data['list'][0]['weather'][0]['id']
   if condition < 900:
       will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        content_sid='xx',
        content_variables='{"1:"409173"}',
        to="whatsapp:+64278419285",
    )

print(will_rain)
