# import Greetings
import Storage
import Helpers
import MyShoppingCart

Helpers.printStock(Storage.storage)

purchases = input('Что выбираешь? ')
quantity = int(input('Какое количество берешь? ')) 

def buy_request(x, y, z):
    for i in x: 
        if i['name'] == y and i['count'] >= z:
            return ('Есть такое')
        continue
    return ('Нет такого')

# Helpers.printStock(Storage.storage)
otvet = buy_request(Storage.storage, purchases, quantity)
print(otvet)

print(('Ты выбрал ') + (purchases) + str(' в количестве ') + str(quantity) + str(' шт! '))
addToShoppingCart = input('Кладём в корзину? да\нет: ')

def addItems():
    MyShoppingCart.shoppingCart.append(purchases)
    print(purchases + ' добавлен в корзину.')

if addToShoppingCart == 'да':
    addItems()
else:
    print('Ну как хочешь.')

pipka = input('Что дальше? \n 1. Посмотреть корзину. \n 2. Удалить товар из корзины. \n 3. Оформить покупку. \n Выбери цифру: ')

def viewCart():
    print('Вот твоя корзина: ' + str(MyShoppingCart.shoppingCart))

def deleteItem():
    MyShoppingCart.shoppingCart.clear()
    print('Корзина очищена ')

def bying():
    viewCart()

if pipka == '1':
    viewCart()
elif pipka == '2':
    deleteItem()
elif pipka == '3':
    bying()
else:
    print('До скорого')


