from telebot import types
import telebot
import Helpers
import Storage
import MyShoppingCart
import copy

current_step = ''
user_choise = dict()
VIEW_ITEM = '1. Посмотреть товар'
VIEW_CART = '2. Посмотреть корзину'
CLEAR_ITEM_FROM_CART = '3. Удалить товар из корзины'
CREATE_ORDER = '4. Оформить заказ'

user_cart = {message.chat.id: MyShoppingCart.shopping_cart}

# def add_orders_by_user_id(user_id, new_item):

# def get_user_cart(user_id):

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
    global current_step
    global user_choise

    if message.text.strip() == VIEW_ITEM:
        Storage.viewStorage(bot, message)
        
    elif message.text.strip() == VIEW_CART:
        MyShoppingCart.getCart(bot, message)
        
    elif message.text.strip() == CLEAR_ITEM_FROM_CART:
        MyShoppingCart.shopping_cart.clear()
        bot.send_message(message.chat.id, 'Корзина очищена ')

    elif message.text.strip() == CREATE_ORDER:
        Storage.viewStorage(bot, message)
        bot.send_message(message.chat.id, 'Что выбираешь? ')
        current_step = 'name'

    elif current_step == 'name':
        # написать функцию проверки имени типа как в Storage и вывести сюда как в переменной Change
        user_choise['name'] = message.text.strip()
        check_in_storage = Helpers.checkInStorage(Storage.storage, user_choise['name'])
        if check_in_storage == True: 
            user_choise['name'] = message.text.strip()
            bot.send_message(message.chat.id, 'Введи количество')
            current_step = 'count'
        else:
            bot.send_message(message.chat.id, 'Такого нет. Введи название еще раз')
            
    elif current_step == 'count':
        user_choise['count'] = int(message.text.strip())
        MyShoppingCart.addItems(copy.copy(user_choise))
        Change = Storage.changeInStorage(Storage.storage, user_choise['name'], user_choise['count'])
        if Change == True:
            answer = ('Ты заказал: ') + (user_choise['name']) + str(' в количестве ') + str((user_choise['count'])) + str(' шт')
            bot.send_message(message.chat.id, answer)
            current_step = False
        else:
            answer = ('Неправильное количество')
            bot.send_message(message.chat.id, answer)
           
        # Прочитать "Копирование по значению, и по ссылке, в чем отличие"
        
while True:  # Запускаем бота
    try:
        bot.polling(none_stop=True)
    except OSError:
        bot.polling(none_stop=True)

