# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

APP_PASSWORD = os.getenv('APP_PASSWORD')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
print(f"This is app password {APP_PASSWORD} and sender mail {SENDER_EMAIL}")
