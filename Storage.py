import Helpers


def changeInStorage(storage, name_item, count):
    for i in storage: 
        if i['name'] == name_item and i['count'] >= count:
            i['count'] = ['count'] - int(quantity)
            print('Количество изменено')
            return True
        continue
    print('Количество не изменено')
    return False

def viewStorage():
    Helpers.printStock(storage)

def checkOrder(check, name_item, count):
    for i in check: 
        if i['name'] == name_item and i['count'] >= count:
            print('Есть такое')
            return True
        continue
    print('Нет такого')
    return False

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
