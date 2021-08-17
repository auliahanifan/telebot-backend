import logging
import time
import telebot
from controller import bot, gateway
from config import IS_PRODUCTION, WEBHOOK_URL, WEBHOOK_PORT, BOT_TOKEN, WEBHOOK_LISTEN
from flask import Flask, request

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

if __name__ == '__main__':
    if IS_PRODUCTION:
        # bot.remove_webhook()
        # time.sleep(0.1)
        # bot.set_webhook(f'{WEBHOOK_URL}/{BOT_TOKEN}')
        app.run(host=WEBHOOK_LISTEN, port=WEBHOOK_PORT)
    else:
        print('Bot Polling Run')
        bot.polling()
