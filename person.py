#Регистрирует и обрабатывает сведения о людях.
#Для тестирования классов из этого файла запустите его напрямую.
from classtools import AttrDisplay # Использовтаь обобщенный интструмент отображения

class Person(AttrDisplay): # Создание класса # Комбинирование с классом верхнего уровня
    #Создает и обрабатывает записи о людях
    # Добавление инициализации полей записи
    def __init__(self, name, job=None, pay=0): # Конструктор принимает 3 аргумента
        self.name = name # Заполнить поля при создании
        self.job = job # self - новый объект экземпляра
        self.pay = pay
    def lastName(self): # Методы реализации поведения. Получение фамилии
        return self.name.split()[1] # Придется изменять код тольо здесь
    def giveRaise(self, percent): # Получение зарплаты
        self.pay = int(self.pay * (1 + percent))
    # def __repr__(self): # Строки для вывода # Вывод информации
    #     return f"[Person: {self.name} {self.pay}]"

class Manager(Person): # Наследование атрибутов Person
    # Настроенная версия Person co специальными требованиями
    # def giveRaise(self, percent, bonus=.10): # Переопределение с целью настройки
    #     self.pay * (1 + percent) + bonus # ЭТО ПЛОХОЙ СПОСОБ! ВЫРЕЗАНИЕ И ВСТАВКА!!!!
    def __init__(self, name, pay):
        Person.__init__(self, name, "mgr", pay)
    def giveRaise(self, percent, bonus=.10): # Повышение зарплаты у руководителя на 10% # Настройка
        Person.giveRaise(self, percent + bonus) # Хороший способ - расширение исходной версии
    def someThingElse(self): # Расширение
        pass


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
    print(jack)
    print(bob)

    tom = Manager("Tom Lorem", 50_000) # Название должности не требуется, оно подразумевается/устанавливается классом
    tom.giveRaise(percent=.10) # Выполняется специальная версия
    print(tom.lastName()) # Выполняется унаследованный метод
    print(tom) # Выполняется унаследованный __repr__
    print(tom.job)

    alina = Person("Alina Krasivaya", "Eng", 50_000)
    alina.giveRaise(.10)
    print(alina)

    print("--- All three ---")
    for obj in (jack, tom, bob):
        obj.giveRaise(.10)
        print(obj)

