import Storage
def printStock(storage):
    for i in Storage.storage: 
        print(('Название: ') + (i['name']), str('в количестве '), + (i['count']), str('шт')) 
