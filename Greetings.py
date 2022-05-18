def sayHello(name):
    print('Привет ' + str(name) + '. Добро пожаловать в магазин! \n 1. Посмотреть товар \n 2. Посмотреть корзину \n 3. Удалить товар из корзины \n 4. Оформить заказ')

def greet():
    name = input('Как тебя зовут? ')
    sayHello(name)
    pipka = input('Выбери действие: ')
    return pipka