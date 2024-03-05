# with open("Day-25/weather_data.csv") as file:
#     weather_data = file.readlines()
# print(weather_data)

# in-built csv library import csv

import csv
import pandas as pd

with open("Day-25/weather_data.csv") as file:
    data = csv.reader(file)
    data
    temperatures = []
    for row in data:
        for col in row:
            temperatures.append(col)

temps = list(map(int, temperatures[4: :3]))

print(temps)

## So much faff
## to install on the windowns powershell - py -m pip install {package name}
## let's do this with pandas



data_pd = pd.read_csv("Day-25/weather_data.csv")

# temp_list = data_pd['temp'].to_list()

# print(sum(temp_list) / len(temp_list))
# print(data_pd['temp'].mean())

# #get col

# data_pd['temp'] # or
# data_pd.temp

## get rows
print(data_pd[data_pd.day == "Monday"])
print(data_pd[data_pd.temp == data_pd.temp.max()])

print(data_pd[data_pd.day == 'Monday']['temp']*(9/5)+32)

## Create dataframe from scratch

squirl_df = pd.read_csv("Day-25/2018_Central_Park_Squirrel_Census.csv")
counts = squirl_df.groupby(['Primary Fur Color'])['Primary Fur Color'].count()

print(counts)








