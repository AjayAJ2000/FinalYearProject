from dotenv import load_dotenv
import os
from django.dispatch import receiver
import telepot
load_dotenv()
def send(message):
    token = os.getenv("TS_TOKEN")
    receiver_id = os.getenv("RECIEVER_ID")
    bot = telepot.Bot(token)
    bot.sendMessage(receiver_id,message)

