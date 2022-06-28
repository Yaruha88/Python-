from telebot import types
import telebot    
import Greetings
import Helpers
from MyShoppingCart import deleteItem, viewCart, addItems
import Storage
import MyShoppingCart

bot = telebot.TeleBot('5202629983:AAHB0cUjCLqJEz8rWs7I-_WHWGLkdYniAX8')
@bot.message_handler(commands=['start'])
def start_message(message):
    # bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    markup.row('1. Посмотреть товар', '2. Посмотреть корзину')
    markup.row('3. Удалить товар из корзины', '4. Оформить заказ')
    # item1 = types.KeyboardButton('1. Посмотреть товар')
    # item2 = types.KeyboardButton('2. Посмотреть корзину')
    # markup.add(item1)
    # markup.add(item2)
    # bot.send_message(message.chat.id, 'Привет! Добро пожаловать! Нажми: \n1. Посмотреть товар\n2. Посмотреть корзину',  reply_markup=markup)
    bot.send_message(message.chat.id, f"""
    Приветствуем Вас, *{message.from_user.first_name}*
    Добро пожаловать! Нажми:
    1. Посмотреть товар
    2. Посмотреть корзину
    3. Удалить товар из корзины
    4. Оформить заказ""", parse_mode="Markdown", reply_markup=markup)
    # bot.send_message(message.chat.id, "{message.chat.username}, Добро пожаловать в магазин! \n 1. Посмотреть товар \n 2. Посмотреть корзину \n 3. Удалить товар из корзины \n 4. Оформить заказ", + message.text)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == '1. Посмотреть товар':
        # markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        # cancel = types.KeyboardButton('Назад')
        # markup.add(cancel)
        for i in Storage.storage: 
            answer = ('Название: ') + (i['name']), str('в количестве '), + (i['count']), str('шт')
            bot.send_message(message.chat.id, answer) 
    elif message.text.strip() == '2. Посмотреть корзину':
        if len(MyShoppingCart.shoppingCart) == 0:
           bot.send_message(message.chat.id, 'Корзина пустая')
        else:
            bot.send_message(message.chat.id, 'В корзине: ')
            for i in Storage.storage:
                incart = ('Название: ') + (i['name']), str('в количестве '), + (i['count']), str('шт')
                bot.send_message(message.chat.id, incart)
        # bot.send_message(message.chat.id, 'Нажми: \n1. Посмотреть товар\n2. Посмотреть корзину')
    elif message.text.strip() == '3. Удалить товар из корзины':
        MyShoppingCart.shoppingCart.clear()
        bot.send_message(message.chat.id, 'Корзина очищена ')
    elif message.text.strip() == '4. Оформить заказ':
        Storage.viewStorage()
        purchases = ('Что выбираешь? ')
        bot.send_message(message.chat.id, purchases)
        quantity = ('Какое количество берешь? ')
        bot.send_message(message.chat.id, quantity)
        if Storage.checkOrder(Storage.storage, purchases, quantity):
            Storage.changeInStorage(Storage.storage, purchases, quantity)
            addItems({'name':purchases, 'count':quantity})
            continueOrdering = ('Заказ оформлен. Хочешь заказать еще? да\нет: ')
            bot.send_message(message.chat.id, continueOrdering)
        if message.text.strip() == 'нет':
            bot.send_message(message.chat.id, 'До свидания')

        
        


# def ordering():
#     Storage.viewStorage()
#     while True:
#         purchases = input('Что выбираешь? ')
#         quantity = int(input('Какое количество берешь? '))
#         if Storage.checkOrder(Storage.storage, purchases, quantity):
#             Storage.changeInStorage(Storage.storage, purchases, quantity)
#             addItems({'name':purchases, 'count':quantity})
#             continueOrdering = input('Заказ оформлен. Хочешь заказать еще? да\нет: ')
        
#         if continueOrdering != 'да':
#             break

# def mainMenu():
#     while True:
#         user_choise = Greetings.greet()
#         if user_choise == '1':
#             Storage.viewStorage()
#         elif user_choise == '2':
#             viewCart()
#         elif user_choise == '3':
#             deleteItem()
#         elif user_choise == '4':
#             ordering()
#         else:
#             print('До скорого')

# name = input('Как тебя зовут? ')
# Greetings.sayHello(name)
# mainMenu()

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




