'''
ПЕРЕГРУЗКА ОПЕРАТОРОВ - переопределение методов
'''
#
# class Car:
#
#     def __init__(self, name):
#         self.name = name
#
#     # перегружаем метод отвечает за метод который превращает какой либо объект в строку
#     def __str__(self):
#         return self.name
#
#     #метод отвечающий за сложение, мы его переопределили
#     def __add__(self, other):
#         return f'{self.name} столкнуся с {other}'
#
#     # Работа с правым объектом 1 + 2 - это будет двойка
#     def __radd__(self, other):
#         pass
#     # Работает с инкрементом +=
#     def __iadd__(self, other):
#         #
#         ...
#     # Диструктор - когда объект удаляется из памяти
#     def __del__(self):
#         print(f'{self.name} was deleted')
#         # это словарь атрибутов
#         self.__dict__[other] = 'dsfsd'
#
#     # Отвечает за работу оператора сравнения
#     def __eq__(self, other):
#         print(f'Сравниваем {self.name} и {other.name}')
#         return
#
#     def __getitem__(self, item):
#         return item ** 2
# zaz = Car('заз')
# ferrari = Car('Ferrari')
# a = Car('ferari')

# a = str(zaz)
#
# print(type(a), a)
# print(type(zaz))

'''Перегрузка употребляется часто для создания библиотек например математических'''

'''Интерфейсы - Совокупность ПУБЛИЧНЫХ методов объекта
Для правильного проектирования интерфейсов это абстрактные классы
'''
#
# from abc import abstractmethod
#
# class Base(ABC):
#
#     @abstractmethod # Именно этот декоратор делает обязательным метод yfl которым располагается
#     def my_method1(self):
#         ...
#
#     def my_method2(self):
#         ...
#
# class Child(Base):
#     ...
#
# a = Child()
#

# Пишем свой итератор

# class Iterator:
#     def __init__(self, start=0):
#         self.i = start
#
#     def __next__(self):
#         self.i += 1
#         if self.i <= 10:
#             return self.i
#         else:
#             raise StopIteration
#
# class IterObj:
#
#     def __init__(self, start=0):
#         self.start = start - 1
#
#     def __iter__(self):
#         return Iterator(self.start)
#
# obj = IterObj
# for el in obj:
#     print(el)

''' @proterty превращает метод в атрибут '''

class User:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    @property # Этот декоратор делает метод атрибутом, то есть его можно вызывать без скобок ()
    def full_name(self):
        return f'{self.name} {self.surname}'
#
# user = User('Tom', 'Crouse')
# print(user.full_name)

''' Композиционный подход '''
# class  CPU:
#     def calc(self):
#         pass
#
# class GPU:
#     pass
#
# class RAM:
#     pass
#
# class Computer:
#
#     def __init__(self):
#         self.cpu = CPU()
#         self.gpu = GPU()
#         self.ram = RAM()
#
#     def process(self):
#         defl.cpu.calc()

'''ДЕКОРАТОР'''
# def my_simple_decorator(function):
#
#     def inner_func():
#         print('Я код который выполняется до')
#         function()
#         print('Этот код выполнился ПОСЛЕ')
#
#     return inner_func()
#
# @my_simple_decorator
# def sum(a=5, b=2):
#     print(a + b)



