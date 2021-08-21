from telebot import types

def markup_main_menu():
    markup = types.ReplyKeyboardMarkup()
    btn_a = types.KeyboardButton('a')
    btn_b = types.KeyboardButton('b')
    markup.row(btn_a, btn_b)
    return markup

def markup_info_menu():
    markup = types.ReplyKeyboardMarkup()
    btn_a = types.KeyboardButton('a')
    btn_b = types.KeyboardButton('b')
    btn_c = types.KeyboardButton('c')
    btn_d = types.KeyboardButton('d')
    btn_e = types.KeyboardButton('e')
    btn_menu = types.KeyboardButton('menu')
    markup.row(btn_a, btn_b)
    markup.row(btn_c, btn_d)
    markup.row(btn_e, btn_menu)
    return markup

def markup_default():
    markup = types.ReplyKeyboardMarkup()
    btn_menu = types.KeyboardButton('menu')
    markup.row(btn_menu)
    return markup

def markup_remove():
    markup = types.ReplyKeyboardRemove(selective=False)
    return markup
