import Helpers

def viewStorage():
    Helpers.printStock(storage)

def checkInStorage(x, y, z):
    for i in x: 
        if i['name'] == y and i['count'] >= z:
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
