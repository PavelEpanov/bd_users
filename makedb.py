from person import Person, Manager # Загрузить класс с помощью from
bob = Person("Bob Alikin") # Использовать имя напрямую
pavel = Person("Pavel Pugachev", job="Developer", pay=175_000)
alina = Manager("Alina Krasivaya", 215_000)

import shelve
db = shelve.open("persondb") # Имя файла, в котором хранятся объекты
for obj in (bob, pavel, alina): # Использовать атрибут name в качестве ключа
    db[obj.name] = obj # Сохранить объект в shelve по ключу
db.close() # Закрыть после внесения изменений

db = shelve.open("persondb") # Заново открыть хранилище
print(len(db)) # Сохранены 3 записи
print(list(db.keys())) # Ключи яввляются индексом
for key in db:
    print(f"key => {db[key]}")
