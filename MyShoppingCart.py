from Helpers import printStock, changeInStorage, checkInStorage

shopping_cart = []

def getCart(bot, message):
    if len(shopping_cart) == 0:
        bot.send_message(message.chat.id, 'Корзина пустая')
    for i in shopping_cart:
        answer = str('Название: ') + str(i['name']) + str(' в количестве ') + str(i['count']) + str(' шт')
        bot.send_message(message.chat.id, answer) 

def viewCart():
    if len(shopping_cart) == 0:
        print('Корзина пустая')
    else:
        print('В корзине: ')
        printStock(shopping_cart)
    
    
def deleteItem():
    shopping_cart.clear()
    print('Корзина очищена ')

def addItems(product):
    exist = checkInStorage(shopping_cart, product['name'])
    if exist:
        changeInStorage(shopping_cart, product['name'], product['count'])
    else:
        shopping_cart.append(product)
    print(product['name'] + ' добавлен в корзину.') 

