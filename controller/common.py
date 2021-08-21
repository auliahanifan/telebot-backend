from helper.bot import bot
from helper.markup import markup_default, markup_main_menu
from helper.status import status
from helper.redis_helper import redis_helper
from text.common_text import text_menu
from text.info_covid import text_info_question_answer_mapping

def send_multiple_msg(list_of_messages, chat_id):
    for msg in list_of_messages:
        bot.send_message(chat_id, msg, reply_markup=markup_default())

def send_answer_covid(chat_id, key):
    answers = text_info_question_answer_mapping[key]
    send_multiple_msg(answers, chat_id)
    redis_helper.set(chat_id, status['other'])

def send_main_menu(chat_id):
    bot.send_message(chat_id, text_menu, reply_markup=markup_main_menu())