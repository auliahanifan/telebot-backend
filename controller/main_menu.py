from helper import bot
from controller.info import send_info_menu
from controller.data import send_data
from controller.screening import switch_screening
import text

def switch_menu(message, latest_user_state):
    msg_txt = message.text
    chat_id = message.chat.id

    if (msg_txt.lower() == 'a'):
        send_data(message)
    elif (msg_txt.lower() == 'b'):
        switch_screening(message, latest_user_state)
    elif (msg_txt.lower() == 'c'):
        send_info_menu(message)
    else:
        bot.send_message(chat_id, text.menu)