from helper.bot import bot
from helper.redis_helper import redis_helper
from helper.status import status
from text.common_text import *
from text.data_covid import *
import requests

@bot.message_handler()
def gateway(message):
    chat_id = message.chat.id
    message_text = message.text.lower()
    user_status = redis_helper.get(chat_id)

    if user_status:
        if message_text == 'a':
            send_current_covid_data(chat_id)
        elif message_text == 'b':
            bot.send_message(chat_id, 'Berikut info mengenai covid')
        else:
            bot.send_message(chat_id, text_menu)

    else:
        redis_helper.set(chat_id, status['menu'])
        bot.send_message(chat_id, text_greeting)
        bot.send_message(chat_id, text_menu)
        
def send_current_covid_data(chat_id):
    full_text_covid = redis_helper.get('full_text_covid')

    if full_text_covid:
        bot.send_message(chat_id, full_text_covid)
    else:
        response = requests.get('https://covid19.mathdro.id/api/countries/indonesia')
        json = response.json()
        confirmed = json['confirmed']['value']
        recovered = json['recovered']['value']
        deaths = json['deaths']['value']

        full_text = text_data_covid.format(confirmed, recovered, deaths)

        redis_helper.set('full_text_covid', full_text, ex=3600)
        bot.send_message(chat_id, full_text)