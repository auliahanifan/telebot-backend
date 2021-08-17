import requests
import text
from helper import bot, redis_helper, Status, pdumps, ChatStatus

def send_data(message):
    chat_id = message.chat.id

    try:
        current_data = redis_helper.get('covid_data')
        if current_data:
            bot.send_message(chat_id, current_data)

        else:
            response = requests.get('https://api.kawalcorona.com/indonesia')
            response = response.json()
            data = response[0]
            resp_text = text.covid_data.format(data['positif'], data['sembuh'], data['meninggal'], data['dirawat'])
            redis_helper.set('covid_data', resp_text, ex=3600)

            bot.send_message(chat_id, resp_text)

        redis_helper.set(str(chat_id), pdumps(ChatStatus(Status.OTHER)))
    except Exception as e:
        bot.send_message(chat_id, text.covid_data_error)
