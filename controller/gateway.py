from telebot import types
from helper.bot import bot
from helper.redis_helper import redis_helper
from helper.status import status
from model.chat import Chat
from text.common_text import *
from text.data_covid import *
from text.info_covid import *
from controller.common import send_main_menu, send_answer_covid
from controller.info_covid import send_current_covid_data, switch_info_covid
from helper.markup import markup_info_menu, markup_remove

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
            switch_main_menu(message_text, chat_id)
            
        elif user_status == status['other']:
            redis_helper.set(chat_id, status['menu'])
            bot.send_message(chat_id, text_greeting)
            send_main_menu(chat_id)

        elif user_status == status['info_covid']:
            switch_info_covid(message_text, chat_id)

    else:
        Chat.get_or_create(id=chat_id)
        redis_helper.set(chat_id, status['menu'])
        bot.send_message(chat_id, text_greeting, reply_markup=markup_remove())
        send_main_menu(chat_id)
        

def switch_main_menu(message_text, chat_id):
    if message_text == 'a':
        send_current_covid_data(chat_id)
    elif message_text == 'b':
        redis_helper.set(chat_id, status['info_covid'])
        bot.send_message(chat_id, text_info_questions_menu, reply_markup=markup_info_menu())
    else:
        send_main_menu(chat_id)