print('У нас есть что-то для тебя! Выбирай: ') 

printStock(storage)
bin = input('Что выбираешь? ')  
q = int(input('Какое количество берешь? ')) 
for i in storage: 
    if i['name'] == bin: 
        if q <= i['count']: 
            i['count'] = i['count'] - q 
            print(('Ты выбрал ') + (bin) + str(' в количестве ') + str(q) + str(' шт! ') + str('Осталось на складе '), + (i['count']), str('шт')) 
        else: 
            print('Слишком дохера, нет столько!') 

printStock(storage)


