from os import name
from telebot import types
import telebot    
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
            answer = ('Название: ') + (i['name']) + str(' в количестве ') + (i['count']) + str(' шт')
            bot.send_message(message.chat.id, answer) 
    elif message.text.strip() == '2. Посмотреть корзину':
        cart = MyShoppingCart.viewCart()
        for i in cart: 
            answer = ('Название: ') + (i['name']) + str(' в количестве ') + str(i['count']) + str(' шт')
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
        PRODUCT['name'] = message.text.strip()
        bot.send_message(message.chat.id, 'Введи количество')
        ODERING = 'count'
    elif ODERING == 'count':
        PRODUCT['count'] = message.text.strip()
        ODERING = False
        answer = ('Ты заказал: ') + (PRODUCT['name']) + str(' в количестве ') + (PRODUCT['count']) + str(' шт')
        bot.send_message(message.chat.id, answer)
        MyShoppingCart.addItems(copy.copy(PRODUCT))
        Change = Storage.changeInStorage(Storage.storage, 'name', 'count')
        for i in Storage.storage: 
            if i['name'] == 'name' and i['count'] >= 'count':
                i['count'] = int(i['count']) + int('count')
                print('Количество изменено')
                return True
            continue
        print('Количество не изменено')
        return False
        # добавить функцию уменьшения из склада
        # Прочитать "Копирование по значению, и по ссылке, в чем отличие"
        
while True:  # Запускаем бота
    try:
        bot.polling(none_stop=True)
    except OSError:
        bot.polling(none_stop=True)

# def order():
#     purchases = input('Что выбираешь? ')
#     quantity = int(input('Какое количество берешь? ')) 
#     otvet = checkInStorage(Storage.storage, purchases, quantity)
#     print(otvet)

#     print(('Ты выбрал ') + (purchases) + str(' в количестве ') + str(quantity) + str(' шт! '))
#     addToShoppingCart = input('Кладём в корзину? да\нет: ')

#     if addToShoppingCart == 'да':
#         addItems()
#     else:
#         print('Ну как хочешь.')
#         Greetings.sayHello(name)
#     return purchases




