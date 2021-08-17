from helper.status import ChatStatus
from helper import bot, redis_helper, send_multiple_msg, Status, pdumps
from controller.common import send_menu
import text

def switch_info(message):
    msg_txt = message.text.lower()
    chat_id = message.chat.id

    if (msg_txt == 'menu'):
        send_menu(chat_id)
        return 
        
    answer = text.info_question_answer_mapping.get(msg_txt, False)
    
    if answer:
        send_multiple_msg(bot, message, answer)
        redis_helper.set(str(chat_id), pdumps(ChatStatus(Status.OTHER)))
    else:
        bot.send_message(chat_id, text.info_questions_menu)
        
def send_info_menu(message):
    chat_id = message.chat.id
    redis_helper.set(str(chat_id), pdumps(ChatStatus(Status.INFO)))
    bot.send_message(chat_id, text.info_questions_menu)