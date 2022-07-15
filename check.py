from person import Person
bob = Person("Bob smith")
print(bob) # Вызывается __repr__ (не __str__) объекта bob
print(bob.__class__) # Показывает класс и его имя для bob
print(bob.__class__.__name__)
print(list(bob.__dict__.keys())) # Атрибуты на самом деле являются ключами словаря

for key in bob.__dict__:
    print(f"key => {bob.__dict__[key]}") # Ручная индексация
print("------")
for key in bob.__dict__:
    print(f"key => {getattr(bob, key)}") # объект.атрибут, но атрибут - переменная