from Helpers import printStock, changeInStorage, checkInStorage

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

def addItems(product):
    exist = checkInStorage(shoppingCart, product['name'])
    if exist:
        changeInStorage(shoppingCart, product['name'], product['count'])
    else:
        shoppingCart.append(product)
    print(product['name'] + ' добавлен в корзину.') 

