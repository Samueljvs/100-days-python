import smtplib
import datetime as dt
import pandas as pd
import random as rnd


## Variables
MONDAY = 2
my_email = 'sammy.verevis@gmail.com'
password = 'xxx'


## Load in data
try:
    data = pd.read_csv('Day-32/quotes_to_use.txt')
except FileNotFoundError:
    org_data = pd.read_csv('Day-32/quotes.txt')
    quote_list = org_data.values.tolist()
else:
    quote_list = data.values.tolist()

if len(quote_list) == 0:
    org_data = pd.read_csv('Day-32/quotes.txt')
    quote_list = org_data.values.tolist()

print(len(quote_list))

# Get test varliable
now = dt.datetime.now().weekday()
today_quote = quote_list.pop(0)

# Conditional test
if MONDAY == now:
    # get today's quote and then remove from list and save it as quotes_to_send
    today_quote = quote_list.pop(0)
    pd.DataFrame(quote_list).to_csv("Day-32/quotes_to_use.txt", index=False)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password )
        connection.sendmail(
            from_addr = my_email, 
            to_addrs = 'sam.verevis@yahoo.com', 
            msg = f"Subject:Quote of the Day\n\n{str(today_quote).strip('[]')}"
            )

## better code below

if MONDAY == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )