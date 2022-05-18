<<<<<<< HEAD
import Greetings
import Helpers
from MyShoppingCart import deleteItem
from MyShoppingCart import viewCart
import Storage


def ordering():
    Storage.viewStorage()
    purchases = input('Что выбираешь? ')
    quantity = int(input('Какое количество берешь? ')) 
    otvet = Storage.checkOrder(Storage.storage, purchases, quantity)
    otvet1 = Storage.changeInStorage(Storage.storage, purchases, quantity)
    print(otvet)
    print(otvet1)
    
    isOrdering = True
    while isOrdering == True:
        zakaz = input('Заказ оформлен. Хочешь заказать еще? да\нет: ')
        if zakaz == 'да':
            ordering()
        else:
            isOrdering = False
        print('До скорого')
    
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
=======
import Greetings
import Helpers
from MyShoppingCart import deleteItem
from MyShoppingCart import viewCart
import Storage


def ordering():
    Helpers.printStock(Storage.storage)
    purchases = input('Что выбираешь? ')
    quantity = int(input('Какое количество берешь? ')) 
    otvet = Storage.checkInStorage(Storage.storage, purchases, quantity)
    print(otvet)
    
    isOrdering = True
    while isOrdering == True:
        zakaz = input('Заказ оформлен. Хочешь заказать еще? да\нет: ')
        if zakaz == 'да':
            ordering()
        else:
            isOrdering = False
        print('До скорого')
    
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




>>>>>>> 27efb3c6f68c5315f6ad54a206bb901bffa5829a
