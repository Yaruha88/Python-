from Helpers import printStock

shoppingCart = []

def viewCart():
    if len(shoppingCart) == 0:
        print('Корзина пустая')
    else:
        print('В корзине: ')
        printStock(shoppingCart)
    
    
def deleteItem():
    shoppingCart.clear()
    print('Корзина очищена ')

def addItems(purchases):
    shoppingCart.append(purchases)
    print(purchases['name'] + ' добавлен в корзину.') 
