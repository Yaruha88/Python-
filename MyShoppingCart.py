from Helpers import printStock

shoppingCart = []

def viewCart():
    printStock(shoppingCart)
    
def deleteItem():
    shoppingCart.clear()
    print('Корзина очищена ')

def addItems(purchases):
    shoppingCart.append(purchases)
<<<<<<< HEAD
    print(purchases + ' добавлен в корзину.')
=======
    print(purchases + ' добавлен в корзину.')
>>>>>>> 27efb3c6f68c5315f6ad54a206bb901bffa5829a
