print('Привет!') 
name = input('Как тебя зовут?') 
print('Привет ' + str(name) + ' и добро пожаловать') 
yes = input('Давай проверим есть ли тебе 18 лет? Да или нет: ') 
if yes == 'Да': 
    print('Молодец, проходи') 
else: 
    print('Иди отсюда, дрищ!') 
print('У нас есть что-то для тебя! Выбирай: ') 
storage = [
{
    'name': 'Вилка',
    'color': 'Красный',
    'count': 10
},
{
    'name': 'Ложка',
    'color': 'Зеленый',
    'count': 5
},
{
    'name': 'Нож',
    'color': 'Синий',
    'count': 1
}
]
def printStock(storage):
    for i in storage: 
        print(('Название: ') + (i['name']), str('в количестве '), + (i['count']), str('шт')) 
printStock(storage)
goods = ['Вилка', 'Ложка', 'Нож']  
bin = input('Что выбираешь? ')  
comment = ['отличный выбор', 'тоже неплохо', 'ну как знаешь'] 
index = goods.index(bin)  
print(comment[index]) 
q = int(input('Какое количество берешь? ')) 
for i in storage: 
    if i['name'] == bin: 
        if q <= i['count']: 
            i['count'] = i['count'] - q 
            print(('Ты выбрал ') + (bin) + str(' в количестве ') + str(q) + str(' шт! ') + str('Осталось на складе '), + (i['count']), str('шт')) 
        else: 
            print('Слишком дохера, нет столько!') 

printStock(storage)


# Helpers.printStock(Storage.storage)

# purchases = input('Что выбираешь? ')
# # choose_color =  input('Какой цвет? ')
# quantity = int(input('Какое количество берешь? ')) 

# def buy_request(x, y, z):
#     for i in x: 
#         if i['name'] == y and i['count'] >= z:
#             return True
#         else:
#             return False


# otvet = buy_request(Storage.storage, purchases, quantity)
# print(otvet)





 # if i['color'] == 'Красный':
    #     i['count'] = 25

# if index_comment == goods[0]:
#     print(comment[0])
# elif index_comment == goods[1]:
#     print(comment[1])
# elif index_comment == goods[2]:
#     print(comment[2])
# else: 
#     print('Нет такого, иди отсюда')
# if bin == goods[0]: 
#     print(comment[0]) 
# elif bin == goods[1]: 
#     print(comment[1]) 
# elif bin == goods[2]: 
#     print(comment[2]) 
# else: 
#     print('Нет такого, иди отсюда')
# storage = [10, 5, 1]
# number = int(input('Выбери количество: '))
# if number in storage > 10:
#     print('Слишком дохера, нет столько! ')


# def order():
#     purchases = input('Что выбираешь? ')
#     quantity = int(input('Какое количество берешь? ')) 
#     otvet = checkInStorage(Storage.storage, purchases, quantity)
#     print(otvet)

#     print(('Ты выбрал ') + (purchases) + str(' в количестве ') + str(quantity) + str(' шт! '))
#     addToShoppingCart = input('Кладём в корзину? да\нет: ')

#     if addToShoppingCart == 'да':
#         addItems()
#     else:
#         print('Ну как хочешь.')
#         Greetings.sayHello(name)
#     return purchases
        
        


# def ordering():
#     Storage.viewStorage()
#     while True:
#         purchases = input('Что выбираешь? ')
#         quantity = int(input('Какое количество берешь? '))
#         if Storage.checkOrder(Storage.storage, purchases, quantity):
#             Storage.changeInStorage(Storage.storage, purchases, quantity)
#             addItems({'name':purchases, 'count':quantity})
#             continueOrdering = input('Заказ оформлен. Хочешь заказать еще? да\нет: ')
        
#         if continueOrdering != 'да':
#             break

# def mainMenu():
#     while True:
#         user_choise = Greetings.greet()
#         if user_choise == '1':
#             Storage.viewStorage()
#         elif user_choise == '2':
#             viewCart()
#         elif user_choise == '3':
#             deleteItem()
#         elif user_choise == '4':
#             ordering()
#         else:
#             print('До скорого')

# name = input('Как тебя зовут? ')
# Greetings.sayHello(name)
# mainMenu()

