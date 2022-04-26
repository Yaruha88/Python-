import Greetings
import Storage
from Storage import storage
import Helpers

purchases = input('Что выбираешь? ')  
quantity = int(input('Какое количество берешь? ')) 
for i in Storage.storage: 
    if i['name'] == purchases: 
        if quantity <= i['count']: 
            i['count'] = i['count'] - quantity 
            print(('Ты выбрал ') + (purchases) + str(' в количестве ') + str(quantity) + str(' шт! ') + str('Осталось на складе '), + (i['count']), str('шт')) 
        else: 
            print('Слишком дохера, нет столько!') 

Helpers.printStock(storage)


