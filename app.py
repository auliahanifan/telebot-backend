import logging
import time
import telebot
import threading
from controller import bot, gateway
from config import IS_PRODUCTION, WEBHOOK_URL, WEBHOOK_PORT, BOT_TOKEN, WEBHOOK_LISTEN
from flask import Flask, request
from model.chat import db, Chat

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

app = Flask(__name__)

# Empty webserver index, return OK, just http 200
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'OK'

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'OK', 200

@app.route(f'/broadcast', methods=['POST'])
def broadcast():
    try:
        chats = Chat.select()
        for chat in chats:
            bot.send_message(chat.id, request.get_json()['message'])
        return 'Ok', 200
    except Exception as e:
        return 'Exception', 200

def bot_polling():
    bot.polling()

if __name__ == '__main__':
    try:
        # Auto create table in DB
        db.create_tables([Chat])
    except Exception as e:
        print('db create table fail')

    if IS_PRODUCTION:
        # Setup Webhook
        bot.remove_webhook()
        time.sleep(0.8)
        bot.set_webhook(f'{WEBHOOK_URL}/{BOT_TOKEN}')
    else:
        # Make sure webhook removed, due to polling is disabled when webhook set
        bot.remove_webhook()
        # Polling running in background
        polling_thread = threading.Thread(target=bot_polling)
        polling_thread.daemon = True
        polling_thread.start()
    
    app.run(host=WEBHOOK_LISTEN, port=WEBHOOK_PORT)

        
