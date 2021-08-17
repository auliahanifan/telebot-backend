from helper import ChatStatus, Screening, Status, redis_helper, pdumps, ploads, bot
from controller.common import send_menu
from text import common_text, screening_text

def switch_screening(message, latest_user_state):
    chat_id = message.chat.id
    msg_text = message.text.lower()

    if latest_user_state.screening is None:
        check_no_screening(chat_id)

    elif type(latest_user_state.screening) is Screening:
        if latest_user_state.screening.phone_number is None:
            check_phone_number(latest_user_state, msg_text, chat_id)

        elif latest_user_state.screening.symptom_high_temp is None:
            check_symptom_high_temp(latest_user_state, msg_text, chat_id)
        
        elif latest_user_state.screening.symptom_cough is None:
            check_symptom_cough(latest_user_state, msg_text, chat_id)

        elif latest_user_state.screening.symptom_hard_to_breath is None:
            check_symptom_hard_to_breath(latest_user_state, msg_text, chat_id)
        
        elif latest_user_state.screening.symptom_anosmia is None:
            check_symptom_anosmia(latest_user_state, msg_text, chat_id)

        elif latest_user_state.screening.contact_patient is None:
            check_contact_patient(latest_user_state, msg_text, chat_id)
        
        elif latest_user_state.screening.contact_suspect is None:
            check_contact_suspect(latest_user_state, msg_text, chat_id)
        
        else:
            send_menu(chat_id)

def check_no_screening(chat_id):
    chat_status = ChatStatus(Status.SCREENING)
    chat_status.screening = Screening()
    redis_helper.set(str(chat_id), pdumps(chat_status))
    bot.send_message(chat_id, screening_text.ask_phone_number)

def check_phone_number(latest_user_state, msg_text, chat_id):
    latest_screening = latest_user_state.screening
    latest_screening.phone_number = msg_text
    latest_user_state.screening = latest_screening

    redis_helper.set(str(chat_id), pdumps(latest_user_state))
    bot.send_message(chat_id, screening_text.symptoms_questions[0])

def check_symptom_high_temp(latest_user_state, msg_text, chat_id):
    latest_screening = latest_user_state.screening
    if msg_text == 'y':
        latest_screening.symptom_high_temp = True
    elif msg_text == 't':
        latest_screening.symptom_high_temp = False
    elif msg_text == 'menu':
        send_menu(chat_id)
        return
    else:
        bot.send_message(chat_id, screening_text.symptoms_questions[0])
        return
    latest_user_state.screening = latest_screening
    redis_helper.set(str(chat_id), pdumps(latest_user_state))
    bot.send_message(chat_id, screening_text.symptoms_questions[1])

def check_symptom_cough(latest_user_state, msg_text, chat_id):
    latest_screening = latest_user_state.screening
    if msg_text == 'y':
        latest_screening.symptom_cough = True
    elif msg_text == 't':
        latest_screening.symptom_cough = False
    elif msg_text == 'menu':
        send_menu(chat_id)
        return
    else:
        bot.send_message(chat_id, screening_text.symptoms_questions[1])
        return
    latest_user_state.screening = latest_screening
    redis_helper.set(str(chat_id), pdumps(latest_user_state))
    bot.send_message(chat_id, screening_text.symptoms_questions[2])

def check_symptom_hard_to_breath(latest_user_state, msg_text, chat_id):
    latest_screening = latest_user_state.screening
    if msg_text == 'y':
        latest_screening.symptom_hard_to_breath = True
    elif msg_text == 't':
        latest_screening.symptom_hard_to_breath = False
    elif msg_text == 'menu':
        send_menu(chat_id)
        return
    else:
        bot.send_message(chat_id, screening_text.symptoms_questions[2])
        return

    is_having_symptomps = False
    if latest_screening.symptom_high_temp:
        is_having_symptomps = True
    if latest_screening.symptom_cough:
        is_having_symptomps = True
    if latest_screening.symptom_hard_to_breath:
        is_having_symptomps = True
    if is_having_symptomps:
        latest_screening.symptom_anosmia = False
        latest_user_state.screening = latest_screening
        redis_helper.set(str(chat_id), pdumps(latest_user_state))
        bot.send_message(chat_id, screening_text.suspections_questions[0])
        return

    latest_user_state.screening = latest_screening
    redis_helper.set(str(chat_id), pdumps(latest_user_state))
    bot.send_message(chat_id, screening_text.symptoms_questions[3])

def check_symptom_anosmia(latest_user_state, msg_text, chat_id):
    latest_screening = latest_user_state.screening

    # is_having_symptomps = False
    # if latest_screening.symptom_high_temp:
    #     is_having_symptomps = True
    # if latest_screening.symptom_cough:
    #     is_having_symptomps = True
    # if latest_screening.symptom_hard_to_breath:
    #     is_having_symptomps = True
    
    # if is_having_symptomps:
    #     latest_screening.symptom_anosmia = False
    # else:
    if msg_text == 'y':
        latest_screening.symptom_anosmia = True
    elif msg_text == 't':
        latest_screening.symptom_anosmia = False
    elif msg_text == 'menu':
        send_menu(chat_id)
        return
    else:
        bot.send_message(chat_id, screening_text.symptoms_questions[3])
        return

    latest_user_state.screening = latest_screening
    redis_helper.set(str(chat_id), pdumps(latest_user_state))
    bot.send_message(chat_id, screening_text.suspections_questions[0])

def check_contact_patient(latest_user_state, msg_text, chat_id):
    latest_screening = latest_user_state.screening
    if msg_text == 'y':
        latest_screening.contact_patient = True
        response = generate_response_from_screening(latest_screening)
        bot.send_message(chat_id, response)
        redis_helper.set(str(chat_id), pdumps(ChatStatus(Status.OTHER)))
        return

    elif msg_text == 't':
        latest_screening.contact_patient = False
    elif msg_text == 'menu':
        send_menu(chat_id)
        return
    else:
        bot.send_message(chat_id, screening_text.suspections_questions[0])
        return
    latest_user_state.screening = latest_screening
    redis_helper.set(str(chat_id), pdumps(latest_user_state))
    bot.send_message(chat_id, screening_text.suspections_questions[1])

def check_contact_suspect(latest_user_state, msg_text, chat_id):
    latest_screening = latest_user_state.screening
    if msg_text == 'y':
        latest_screening.contact_suspect = True
    elif msg_text == 't':
        latest_screening.contact_suspect = False
    elif msg_text == 'menu':
        send_menu(chat_id)
        return
    else:
        bot.send_message(chat_id, screening_text.suspections_questions[1])
        return
    latest_user_state.screening = latest_screening

    response = generate_response_from_screening(latest_screening)
    bot.send_message(chat_id, response)
    redis_helper.set(str(chat_id), pdumps(ChatStatus(Status.OTHER)))

def generate_response_from_screening(screening):
    symtomps = []
    risk_level = "rendah"

    response = ""

    if screening.symptom_high_temp:
        symtomps.append("demam tinggi")
    if screening.symptom_cough:
        symtomps.append("batuk")
    if screening.symptom_hard_to_breath:
        symtomps.append("sesak dan sulit bernafas")
    if screening.contact_patient:
        risk_level = "tinggi"
    if screening.contact_suspect:
        risk_level = "sedang"
    
    if len(symtomps) > 0:
        response += f"Baik, karena saat ini mengalami {', '.join(symtomps)} "
    elif len(symtomps) == 0:
        response += f"Baik, karena saat ini tidak mengalami demam tinggi, batuk, sedak dan sulit bernafas "

    if risk_level == "tinggi":
        response += "serta pernah kontak dengan pasien covid, "
    elif risk_level == "sedang":
        response += "serta pernah kontak dengan orang yang memiliki gejala flu atau diduga terkena virus Corona, "
    elif risk_level == "rendah":
        response += "serta tidak pernah kontak dengan pasien covid ataupun orang yang memiliki gejala flu atau diduga terkena virus Corona, "

    response += f"maka resiko tertular anda adalah *{risk_level}*"

    return response
