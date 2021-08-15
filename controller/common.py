from helper import bot, redis_helper, Status
import text

def send_menu(chat_id):
    redis_helper.set(str(chat_id), str(Status.MAIN_MENU))
    bot.send_message(chat_id, text.menu)