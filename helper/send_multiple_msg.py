def send_multiple_msg(bot, message, txt_list):
    for txt in txt_list:
        bot.send_message(message.chat.id, txt)