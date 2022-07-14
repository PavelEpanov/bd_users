class Person: # Создание класса
    # Добавление инициализации полей записи
    def __init__(self, name, job=None, pay=0): # Конструктор принимает 3 аргумента
        self.name = name # Заполнить поля при создании
        self.job = job # self - новый объект экземпляра
        self.pay = pay
    def lastName(self): # Методы реализации поведения
        return self.name.split()[1] # Придется изменять код тольо здесь
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


if __name__ == "__main__":
    bob = Person("Bob Smith")
    jack = Person("Jack Fedunkin", "developer", 567)
    print(bob.name, bob.job)
    print(jack.name, jack.job, jack.pay)
    # print(bob.name.split()[1]) # Извлечение фамилии из лбъекта
    # jack.pay *= 1.10 # Предоставление этому объекту повышения
    # print(jack.pay)
    print(bob.lastName(), jack.lastName())
    jack.giveRaise(.10)
    print(jack.pay)
