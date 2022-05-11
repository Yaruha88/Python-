import Greetings
import Storage
import Helpers
import MyShoppingCart
# коммент111

def viewStorage():
    Helpers.printStock(Storage.storage)
    
def viewCart():
    print('Вот твоя корзина: ' + str(MyShoppingCart.shoppingCart))

def addItems():
    MyShoppingCart.shoppingCart.append(purchases)
    print(purchases + ' добавлен в корзину.')

def deleteItem():
    MyShoppingCart.shoppingCart.clear()
    print('Корзина очищена ')

def ordering():
    isOrdering = True
    while isOrdering == True:
        zakaz = input('Заказ оформлен. Хочешь заказать еще? да\нет: ')
        if zakaz == 'да':
            print(Helpers.printStock(Storage.storage))
        else:
            isOrdering = False
        print('До скорого')

def buy_request(x, y, z):
    for i in x: 
        if i['name'] == y and i['count'] >= z:
            print('Есть такое')
            return True
        continue
    print('Нет такого')
    return False

if Greetings.pipka == '1':
    viewStorage()
elif Greetings.pipka == '2':
    viewCart()
elif Greetings.pipka == '3':
    deleteItem()
elif Greetings.pipka == '4':
    ordering()
else:
    print('До скорого')

purchases = input('Что выбираешь? ')
quantity = int(input('Какое количество берешь? ')) 
otvet = buy_request(Storage.storage, purchases, quantity)
print(otvet)

print(('Ты выбрал ') + (purchases) + str(' в количестве ') + str(quantity) + str(' шт! '))
addToShoppingCart = input('Кладём в корзину? да\нет: ')

if addToShoppingCart == 'да':
    addItems()
else:
    print('Ну как хочешь.')


