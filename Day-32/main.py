##################### Normal Starting Project ######################

import pandas as pd
import datetime  as dt
import random as rnd
import smtplib

my_email = 'sammy.verevis@gmail.com'
password = 'ivya lfit jrmw glii'


df = pd.read_csv("Day-32/birthdays.csv")

df.set_index(["month", "day"], inplace=True)
bd_dict = {
    index: row.to_dict() for (index, row) in df.iterrows()}

today = (dt.datetime.now().month, dt.datetime.now().day)

if(today) in bd_dict:
    name = bd_dict[today]['name'] # get name for letter
    with open(f"Day-32/letter_templates/letter_{rnd.randrange(1,4)}.txt") as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() 
        connection.login(user = my_email, password = password )
        connection.sendmail(
            from_addr = my_email, 
            to_addrs = 'sam.verevis@yahoo.com', 
            msg = f"Subject:Happy Birthday {name}!\n\n{letter}"
            )

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



