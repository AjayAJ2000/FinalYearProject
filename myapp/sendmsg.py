
from django.dispatch import receiver
import telepot
def send(message):
    token = "5519372105:AAGPYexmU0KyZZzSIatdz374p5sMtWseJAo"
    receiver_id = 914139390
    bot = telepot.Bot(token)
    bot.sendMessage(receiver_id,message)

