import shelve

db = shelve.open("persondb") # снова открыть хрналище с тем же именем
for key in sorted(db): # Проход для отображения объектов из базы данных
    print(f"Key => {db[key]}")
alina = db["Alina Krasivaya"] # Индесация по ключу с целью извлечения
alina.giveRaise(.10) # Обновление в памяти, используя метод класса
db["Alina Krasivaya"] = alina # Присваивание по ключу для обновления в хранилище shelve
db.close() # Закрытие после внесения измнений