from os import stat
from helper.bot import bot
from helper.redis_helper import redis_helper
from helper.status import status
from text.common_text import *
from text.data_covid import *
from text.info_covid import *
import requests

@bot.message_handler()
def gateway(message):
    chat_id = message.chat.id
    message_text = message.text.lower()
    
    user_status = None
    try:
        user_status = redis_helper.get(chat_id).decode("utf-8") 
    except:
        pass

    if user_status:
        if user_status == status['menu']:
            if message_text == 'a':
                send_current_covid_data(chat_id)
            elif message_text == 'b':
                redis_helper.set(chat_id, status['info_covid'])
                bot.send_message(chat_id, text_info_questions_menu)
            else:
                bot.send_message(chat_id, text_menu)

        elif user_status == status['other']:
            redis_helper.set(chat_id, status['menu'])
            bot.send_message(chat_id, text_greeting)
            bot.send_message(chat_id, text_menu)

        elif user_status == status['info_covid']:
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
                bot.send_message(chat_id, text_menu)

            else:
                bot.send_message(chat_id, text_info_questions_menu)

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

def send_multiple_msg(list_of_messages, chat_id):
    for msg in list_of_messages:
        bot.send_message(chat_id, msg)

def send_answer_covid(chat_id, key):
    answers = text_info_question_answer_mapping[key]
    send_multiple_msg(answers, chat_id)
    redis_helper.set(chat_id, status['other'])
