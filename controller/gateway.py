from helper import bot, redis_helper, Status, ploads
from controller.info import switch_info
from controller.main_menu import switch_menu
from controller.screening import switch_screening
from controller.common import send_menu
import text

@bot.message_handler()
def gateway(message):
    chat_id = message.chat.id
    latest_user_state = None
    try:
        latest_user_state = ploads(redis_helper.get(str(chat_id)))
        print(latest_user_state.to_json())
    except Exception as e:
        print(f'Exception in Checking ploads {e}') 

    if latest_user_state:
        main_switch(message, latest_user_state)
    else:
        bot.send_message(chat_id, text.greeting)
        send_menu(chat_id)

def main_switch(message, latest_user_state):
    chat_id = message.chat.id

    if (latest_user_state.status == Status.MAIN_MENU):
        switch_menu(message, latest_user_state)
    elif (latest_user_state.status == Status.INFO):
        switch_info(message)
    elif (latest_user_state.status == Status.SCREENING):
        switch_screening(message, latest_user_state)
    else:
        send_menu(chat_id)

