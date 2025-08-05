import requests
import datetime  as dt
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## email 
my_email = 'sammy.verevis@gmail.com'
password = ''


## get telsa stock price
stock_api = '9W4AD8QU8N5DFIJ0'
stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "outputsize":"compact",
    "apikey" : stock_api
}

## News Data
news_api = "d2d62d6ea83c4bcb8edc8614b146ddaa"
news_parameters ={
    "apiKey":news_api,
    "qInTitle":"Tesla",
    "pageSize":3,
}

# # get data
# Stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
# Stock_response.raise_for_status()
# stock_data = Stock_response.json()['Time Series (Daily)']
# data_list = [value for (key,value) in stock_data.items()]

# yester_p = data_list[0]['4. close']
# two_day_p = data_list[1]['4. close']
# diff = ((yester_p - two_day_p)/yester_p) *100

## get newws
news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()['articles']

# with list comp
top_3 = news_data[0:3]

email_body = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in top_3]

print(email_body)

#one way with for loop
email_message = []
for i in range(0,3):
    title = news_data[i]['title']
    content = news_data[i]['description']
    url = news_data[i]['url']
    email_message.append(title+content+url)

# ## send email
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user = my_email, password = password )
#     connection.sendmail(
#         from_addr = my_email, 
#         to_addrs = 'sam.verevis@yahoo.com', 
#         msg = f"Subject:Telsa Stock News\n\n Tesla is up \n{email_message[0]}\n{email_message[1]}\n{email_message[2]}"
#         )


#. strip('[]')
# get_news = False

# if diff > 2:
#     print("Get News")
#     get_news = True

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator





## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

