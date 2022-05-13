from Helpers import printStock

shoppingCart = []

def viewCart(shoppingCart):
    printStock(shoppingCart)
    
def deleteItem():
    shoppingCart.clear()
    print('Корзина очищена ')

def addItems(purchases):
    shoppingCart.append(purchases)
    print(purchases + ' добавлен в корзину.')
