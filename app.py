import threading
import telebot
import time
from config import BOT_TOKEN, IS_PRODUCTION, WEBHOOK_URL
from helper.bot import bot
from model.chat import Chat
from controller.gateway import gateway
from flask import Flask, request, jsonify

app = Flask(__name__)

def bot_polling():
    while True:
        try:
            bot.polling()
        except:
            pass

# Empty webserver index, return OK, just http 200
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'OK'

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'OK', 200

@app.route('/broadcast', methods=['POST'])
def broadcast():
    try:
        message = request.get_json()['message']
        chats = Chat.select()
        for chat in chats:
            bot.send_message(chat.id, message)
        return 'Ok'
    except:
        return 'Failed'

if __name__ == '__main__':
    if IS_PRODUCTION:
        bot.remove_webhook()
        time.sleep(0.8)
        bot.set_webhook(f'{WEBHOOK_URL}/{BOT_TOKEN}')
    else:
        bot.remove_webhook()
        # Polling running in background
        polling_thread = threading.Thread(target=bot_polling)
        polling_thread.daemon = True
        polling_thread.start()
    app.run('0.0.0.0', port=8000)