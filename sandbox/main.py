from datetime import datetime as dt

month = dt.now().month
day = dt.now().weekday()

time = dt.now().time()

date_1= dt.strptime("2025-08-19", "%Y-%m-%d")

print(month)
print(day)

print(time)

print(dt.weekday(date_1))


