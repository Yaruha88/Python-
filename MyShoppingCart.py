shoppingCart = []

def viewCart():
    for i in shoppingCart: 
        print('Вот твоя корзина: ' + str(i))

def deleteItem():
    shoppingCart.clear()
    print('Корзина очищена ')

def addItems(purchases):
    shoppingCart.append(purchases)
    print(purchases + ' добавлен в корзину.')
