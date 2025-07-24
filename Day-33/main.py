import requests
from datetime import datetime
import smtplib
import time

my_email = 'sammy.verevis@gmail.com'
password = 'xxx'

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])

iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

hour_now = datetime.now().hour

hour_now = 2
iss_latitude = 50.4523
iss_longitude = -0.3425

# a function to assess if should send email or not
def send_email():
    if abs(iss_latitude - MY_LAT) <=5 and abs(iss_longitude - MY_LONG) <= 5 and hour_now > sunset or hour_now < sunrise:
        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls() 
                connection.login(user = my_email, password = password )
                connection.sendmail(
                    from_addr = my_email, 
                    to_addrs = 'sam.verevis@yahoo.com', 
                    msg = f"Subject:Look up!!\n\n The ISS international space station is right above you!!!!"
                    )
count = 0

while True:
    send_email()
    count =+ 1
    

    if count == 2:
        print("Breaking out")
        break  

    time.sleep(60) 
     
     
#If the ISS is close to my current position


# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



