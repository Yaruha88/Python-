def printStock(storage):
    for i in storage: 
        print(('Название: ') + (i['name']), str('в количестве '), + (i['count']), str('шт')) 

def changeInStorage(storage, name_item, count):
    for i in storage: 
        if i['name'] == name_item:
            i['count'] = i['count'] + count
            print('Количество в корзине изменено')
            return True
        continue
    print('Количество в корзине не изменено')
    return False

def checkInStorage(check, name_item):
    for i in check: 
        if i['name'] == name_item:
            print('Есть такое')
            return True
        continue
    print('Нет такого')
    return False
