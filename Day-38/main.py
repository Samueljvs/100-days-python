import requests
import os
from requests.auth import HTTPBasicAuth
from datetime import datetime as dt


APP_ID = os.getenv("NUTRIX_APP_ID")
API_KEY = os.getenv("NUTRIX_API_ID")

USERNAME = 'sam'
PASSWORD = os.getenv("PASSWORD_WORKOUT_SHEET")

NUTRIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

header_nutrix = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

text_q = input("What exercise did you do today? ")

nutrix_config = {
    "query":text_q
}

response = requests.post(url=NUTRIX_ENDPOINT, json=nutrix_config, headers=header_nutrix)
response.raise_for_status()
data = response.json()['exercises']

current_date = dt.now().strftime("%d/%m/%Y")
current_time = dt.now().time().strftime("%H:%M")
exercise = data[0]['name']
durat = data[0]['duration_min']
cal = data[0]['nf_calories']

## Sheety google sheets API
workout_sheet_endpoint = "https://api.sheety.co/047a4bce014f4b09e1f0dd3914c08af7/myWorkout/workout"

new_row = {
    "workout": {  # The key must match the name of your sheet/tab in lowercase
        "date": current_date,
        "time": current_time,
        "exercise": exercise,
        "duration": durat,
        "calories": cal
    }
}
response = requests.post(url = workout_sheet_endpoint, json= new_row, auth=(USERNAME, PASSWORD))
response.raise_for_status()

print("Status:", response.status_code)
print("Response:", response.text)