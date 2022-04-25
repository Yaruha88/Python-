print('У нас есть что-то для тебя! Выбирай: ') 

printStock(storage)
purchases = input('Что выбираешь? ')  
quantity = int(input('Какое количество берешь? ')) 
for i in storage: 
    if i['name'] == purchases: 
        if quantity <= i['count']: 
            i['count'] = i['count'] - quantity 
            print(('Ты выбрал ') + (purchases) + str(' в количестве ') + str(quantity) + str(' шт! ') + str('Осталось на складе '), + (i['count']), str('шт')) 
        else: 
            print('Слишком дохера, нет столько!') 

printStock(storage)


