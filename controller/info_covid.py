import requests
from helper.redis_helper import redis_helper
from helper.bot import bot
from helper.status import status
from text.info_covid import text_info_questions_menu
from text.data_covid import *
from controller.common import send_main_menu, send_answer_covid


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

def switch_info_covid(message_text, chat_id):
    if message_text == 'a':
        send_answer_covid(chat_id, 'a')

    elif message_text == 'b':
        send_answer_covid(chat_id, 'b')

    elif message_text == 'c':
        send_answer_covid(chat_id, 'c')

    elif message_text == 'd':
        send_answer_covid(chat_id, 'd')

    elif message_text == 'e':
        send_answer_covid(chat_id, 'e')

    elif message_text == 'menu':
        # ganti status jadi menu dan kirim text menu
        redis_helper.set(chat_id, status['menu'])
        send_main_menu(chat_id)

    else:
        bot.send_message(chat_id, text_info_questions_menu)
