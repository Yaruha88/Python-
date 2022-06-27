from telebot import types
import telebot    
import Greetings
import Helpers
from MyShoppingCart import deleteItem, viewCart, addItems
import Storage


bot = telebot.TeleBot('5202629983:AAHB0cUjCLqJEz8rWs7I-_WHWGLkdYniAX8')
@bot.message_handler(commands=['start'])
def start_message(message):
    # bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('1. Посмотреть товар')
    item2 = types.KeyboardButton('2. Посмотреть корзину')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',  reply_markup=markup)
    # bot.send_message(message.chat.id, "{message.chat.username}, Добро пожаловать в магазин! \n 1. Посмотреть товар \n 2. Посмотреть корзину \n 3. Удалить товар из корзины \n 4. Оформить заказ", + message.text)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == '1. Посмотреть товар':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        cancel = types.KeyboardButton('Назад')
        markup.add(cancel)
        for i in Storage.storage: 
            answer = ('Название: ') + (i['name']), str('в количестве '), + (i['count']), str('шт')
            bot.send_message(message.chat.id, answer, reply_markup=markup) 
        # bot.send_message(message.chat.id, 'Привет')
        
        


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




