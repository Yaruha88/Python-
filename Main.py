from os import name
import Greetings
import Storage
import Helpers
import MyShoppingCart



def viewStorage():
    Helpers.printStock(Storage.storage)

def viewCart():
    print('Вот твоя корзина: ' + str(MyShoppingCart.shoppingCart))

def deleteItem():
    MyShoppingCart.shoppingCart.clear()
    print('Корзина очищена ')

def addItems(purchases):
    MyShoppingCart.shoppingCart.append(purchases)
    print(purchases + ' добавлен в корзину.')

def ordering():
    Helpers.printStock(Storage.storage)
    purchases = input('Что выбираешь? ')
    quantity = int(input('Какое количество берешь? ')) 
    otvet = checkInStorage(Storage.storage, purchases, quantity)
    print(otvet)
    
    isOrdering = True
    while isOrdering == True:
        zakaz = input('Заказ оформлен. Хочешь заказать еще? да\нет: ')
        if zakaz == 'да':
            ordering()
        else:
            isOrdering = False
        print('До скорого')
    
def checkInStorage(x, y, z):
    for i in x: 
        if i['name'] == y and i['count'] >= z:
            print('Есть такое')
            return True
        continue
    print('Нет такого')
    return False

user_choise = Greetings.greet()

if user_choise == '1':
    viewStorage()
elif user_choise == '2':
    viewCart()
elif user_choise == '3':
    deleteItem()
elif user_choise == '4':
    ordering()
else:
    print('До скорого')

