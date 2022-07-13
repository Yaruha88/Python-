# -*- coding: utf-8 -*-
from telebot import types
import telebot
import Helpers
import Storage
import MyShoppingCart
import copy
ODERING = ''
PRODUCT = dict()

bot = telebot.TeleBot('5202629983:AAHB0cUjCLqJEz8rWs7I-_WHWGLkdYniAX8')
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    markup.row('1. Посмотреть товар', '2. Посмотреть корзину')
    markup.row('3. Удалить товар из корзины', '4. Оформить заказ')
    bot.send_message(message.chat.id, f"""
    Приветствуем Вас, *{message.from_user.first_name}*
    Добро пожаловать! Нажми:
    1. Посмотреть товар
    2. Посмотреть корзину
    3. Удалить товар из корзины
    4. Оформить заказ""", parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    global ODERING
    global PRODUCT

    if message.text.strip() == '1. Посмотреть товар':
        for i in Storage.storage: 
            answer = ('Название: ') + (i['name']) + str(' в количестве ') + str(i['count']) + str(' шт')
            bot.send_message(message.chat.id, answer) 
    elif message.text.strip() == '2. Посмотреть корзину':
        cart = MyShoppingCart.getCart()
        if len(cart) == 0:
            bot.send_message(message.chat.id, 'Корзина пустая')
        for i in cart:
            answer = str('Название: ') + str(i['name']) + str(' в количестве ') + str(i['count']) + str(' шт')
            bot.send_message(message.chat.id, answer) 
    elif message.text.strip() == '3. Удалить товар из корзины':
        MyShoppingCart.shoppingCart.clear()
        bot.send_message(message.chat.id, 'Корзина очищена ')
    elif message.text.strip() == '4. Оформить заказ':
        for i in Storage.storage: 
            answer = ('Название: ') + (i['name']) + str(' в количестве ') + str(i['count']) + str(' шт')
            bot.send_message(message.chat.id, answer) 
        bot.send_message(message.chat.id, 'Что выбираешь? ')
        ODERING = 'name'
    elif ODERING == 'name':
        # написать функцию проверки имени типа как в Storage и вывести сюда как в переменной Change
        PRODUCT['name'] = message.text.strip()
        Check = Helpers.checkInStorage(Storage.storage, PRODUCT['name'])
        if Check == True: 
            PRODUCT['name'] = message.text.strip()
            bot.send_message(message.chat.id, 'Введи количество')
            ODERING = 'count'
        else:
            bot.send_message(message.chat.id, 'Такого нет. Введи название еще раз')
    elif ODERING == 'count':
        PRODUCT['count'] = int(message.text.strip())
        MyShoppingCart.addItems(copy.copy(PRODUCT))
        Change = Storage.changeInStorage(Storage.storage, PRODUCT['name'], PRODUCT['count'])
        if Change == True:
            answer = ('Ты заказал: ') + (PRODUCT['name']) + str(' в количестве ') + str((PRODUCT['count'])) + str(' шт')
            bot.send_message(message.chat.id, answer)
            ODERING = False
        else:
            answer = ('Неправильное количество')
            bot.send_message(message.chat.id, answer)
           
        # Прочитать "Копирование по значению, и по ссылке, в чем отличие"
        
while True:  # Запускаем бота
    try:
        bot.polling(none_stop=True)
    except OSError:
        bot.polling(none_stop=True)

