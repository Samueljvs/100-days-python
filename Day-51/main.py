from dotenv import load_dotenv
import os
import Bot


load_dotenv(dotenv_path="Day-51/.env")  # Manually load .env

PROMISED_UP = 150
PROMISED_DOWN = 10
CHROME_DRIVER_PATH = '/Users/Samuel/Development/chromedriver'
USER_EMAIL = os.getenv('XEMAIL')
USER_PASS = os.getenv('XPASS')

sam_bot = Bot.InternetSpeedTwitterBot()

#sam_bot.get_internet_speed()
sam_bot.tweet_at_provider(USER_EMAIL, USER_PASS)

