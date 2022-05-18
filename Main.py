import Greetings
import Helpers
from MyShoppingCart import deleteItem, viewCart
import Storage


def ordering():
    Storage.viewStorage()
    purchases = input('Что выбираешь? ')
    quantity = int(input('Какое количество берешь? ')) 
    otvet = Storage.checkOrder(Storage.storage, purchases, quantity)
    otvet1 = Storage.changeInStorage(Storage.storage, purchases, quantity)
    print(otvet)
    print(otvet1)
    
    isOrdering = True
    while isOrdering == True:
        zakaz = input('Заказ оформлен. Хочешь заказать еще? да\нет: ')
        if zakaz == 'да':
            ordering()
        else:
            isOrdering = False
        print('До скорого')
    
user_choise = Greetings.greet()

if user_choise == '1':
    Storage.viewStorage()
elif user_choise == '2':
    viewCart()
elif user_choise == '3':
    deleteItem()
elif user_choise == '4':
    ordering()
else:
    print('До скорого')
