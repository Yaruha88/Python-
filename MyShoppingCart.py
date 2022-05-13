import Helpers
import Storage


shoppingCart = []

def viewStorage():
    Helpers.printStock(Storage.storage)

def viewCart():
    print('Вот твоя корзина: ' + str(shoppingCart))

def deleteItem():
    shoppingCart.clear()
    print('Корзина очищена ')

def addItems(purchases):
    shoppingCart.append(purchases)
    print(purchases + ' добавлен в корзину.')
