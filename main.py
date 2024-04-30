# #Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін
from abc import ABC, abstractmethod

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __len__(self):
        return (self.x + self.y) * 2

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()


rec1 = Rectangle(10, 20)
rec2 = Rectangle(12, 22)

# print(rec1.area())
# print(rec2.area())
# print(rec1 + rec2)
# print(rec1 - rec2)
# print(rec1 == rec2)
# print(rec1 != rec2)
# print(rec1 > rec2)
# print(rec1 < rec2)
# print(len(rec1))

# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Cinderella(Human):
    counter = 0
    def __init__(self,name,age,foot_size):
        super().__init__(name,age)
        self.foot_size = foot_size
        Cinderella.counter += 1

    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def get_count(cls):
        return cls.counter



class Prince(Human):
    def __init__(self,name,age,found_size):
        super().__init__(name,age)
        self.found_size = found_size

    def searching(self,princess: list[Cinderella]) -> None:
        for prince in princess:
            if prince.foot_size == self.found_size:
                print(prince)
                return

pr1 = Prince('Roberto',20,38)
c1 = Cinderella('Alina',18,39)
c2 = Cinderella('Margo',19,42)
c3 = Cinderella('Sofia',20,38)

cinderellas_list = [
    c1,c2,c3
]
pr1.searching(cinderellas_list)
print(c1.get_count())


# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

class Printable(ABC):

    @abstractmethod
    def print_(self):
        pass

class Book(Printable):
    def __init__(self,name):
        self.name = name

    def print_(self):
        print( f'The book {self.name} is')

class Magazine(Printable):
    def __init__(self,name):
        self.name = name

    def print_(self):
        print( f'The magazine {self.name} is')


# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом
# Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
class Main():
    printable_list: list[Printable] = []
    def __init__(self,name):
        self.name = name

    @classmethod
    def add_(cls,item):
        if isinstance(item,Printable):
            cls.printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for magazine in cls.printable_list:
            if isinstance(magazine,Magazine):
               magazine.print_()

    @classmethod
    def show_all_books(cls):
        for book in cls.printable_list:
            if isinstance(book,Book):
                book.print_()


Main.add_(Book('Koob1'))
Main.add_(Magazine('kekes1'))
Main.add_(Book('Moob2'))
Main.add_(Book('Kook3'))
Main.add_(Magazine('kekesh2'))

Main.show_all_magazines()
Main.show_all_books()

import sqlite3
sqlite_version = sqlite3.sqlite_version
sqlite_version_info = sqlite3.sqlite_version_info
threadsafety = sqlite3.threadsafety
print([sqlite_version, sqlite_version_info, threadsafety])

# Для Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32:
# ['3.43.1', (3, 43, 1), 3]