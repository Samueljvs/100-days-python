from dotenv import load_dotenv
import os

load_dotenv()  # Manually load .env

key = os.getenv("NUTRIX_APP_ID")

print(key)