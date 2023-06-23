import random

import telebot
from telebot import types
import os

bot = telebot.TeleBot('6267142880:AAGq8wHVsyUr98y-gITdlU46xt4SK23bDIs')


def get_name(from_user):
    name = str(from_user.first_name) + ' ' + str(from_user.last_name)
    if name.endswith('None'):
        name = name[:-5]
    return name


@bot.message_handler(commands=['start'])
def start(message):
    name = get_name(message.from_user)

    receive = f'Привет <b>{name}</b>'
    bot.send_message(message.from_user.id, receive, parse_mode='html')


@bot.message_handler(commands=['help'])
def get_text_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    start_btn = types.KeyboardButton("/start")
    welcome_btn = types.KeyboardButton("/hi")
    website_btn = types.KeyboardButton("/website")
    photo_btn = types.KeyboardButton("/photo")

    markup.add(start_btn, welcome_btn, website_btn, photo_btn)
    bot.send_message(message.from_user.id, "Выбери нужную команду", reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.from_user.id, 'Интересное фото!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://google.com"))
    bot.send_message(message.from_user.id, "Вебсайт...", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == "/hi":
        name = get_name(message.from_user)
        receive = f'Привет <b>{name}</b>, чем могу помочь?'
        bot.send_message(message.from_user.id, receive, parse_mode='html')
    elif message.text.lower() == "/photo":
        filelist = os.listdir("photo")
        photo = open(f'photo/{random.choice(filelist)}', 'rb')

        bot.send_photo(message.from_user.id, photo)
    else:
        bot.send_message(message.from_user.id, 'Неизвестная команда. Напиши /help для вызова справки')


bot.polling(none_stop=True, timeout=0)
