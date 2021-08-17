from helper import bot, redis_helper, Status, pdumps, ChatStatus
import text

def send_menu(chat_id):
    redis_helper.set(str(chat_id), pdumps(ChatStatus(Status.MAIN_MENU)))
    bot.send_message(chat_id, text.menu)