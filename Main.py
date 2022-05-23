import Greetings
import Helpers
from MyShoppingCart import deleteItem, viewCart, addItems
import Storage


def ordering():
    Storage.viewStorage()
    while True:
        purchases = input('Что выбираешь? ')
        quantity = int(input('Какое количество берешь? '))
        if Storage.checkOrder(Storage.storage, purchases, quantity):
            Storage.changeInStorage(Storage.storage, purchases, quantity)
            addItems({'name':purchases, 'count':quantity})
            continueOrdering = input('Заказ оформлен. Хочешь заказать еще? да\нет: ')
        
        if continueOrdering != 'да':
            break

def mainMenu():
    while True:
        user_choise = Greetings.greet()
        if user_choise == '1':
            Storage.viewStorage()
        elif user_choise == '2':
            viewCart()
        elif user_choise == '3':
            deleteItem()
        elif user_choise == '4':
            ordering()
        else:
            print('До скорого')

name = input('Как тебя зовут? ')
Greetings.sayHello(name)
mainMenu()
