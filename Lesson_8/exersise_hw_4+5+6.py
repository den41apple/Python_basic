'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''
from abc import ABC, abstractmethod
from time import sleep


class OfficeEquipmentWarehouse:
    _storage = {'Printer': 0,
                'Scanner': 0,
                'Xerox': 0
                }
    max_capasity = 100

    departaments = {1: 'Логистический отдел',
                    2: 'Отдел контроля качества',
                    3: 'Отдел ремонта техники',
                    4: 'Склад хранения'
                    }

    @classmethod
    def checking_capasity(cls):
        quantity = 0
        for i in cls._storage.keys():
            quantity += cls._storage[i]
            if quantity > cls.max_capasity:
                print('Склад переполнен')
                break
        print(f'На складе {cls.max_capasity - quantity}')

    @classmethod
    def moving_to_warehouse(cls, name, quantity=1):
        print(f'Запрос принятия {name}:')

        print('В какой отдел хотите отправить: ')
        for i in sorted(cls.departaments.keys()):
            print(f'{i} : {cls.departaments[i]}')
        try:
            departament = int(input('Номер: '))
            cls._storage[name] += quantity
        except ValueError as err:
            print(f'Необходимо было ввести число, переместить на {cls.departaments[4]}?')
            if (input('Д(Да) / Н(Нет) : ')).upper() == 'Д':
                departament = 4
            else:
                print(f'Прием {name} отклонен')
                return None

        print(f'Printer принят в "{cls.departaments[departament]}" в количестве {quantity} шт')


class OfficeEquipment(ABC):
    @abstractmethod
    def what_i_can_do(self):
        ...

    @abstractmethod
    def moving_to_warehouse(self):
        ...
    @abstractmethod
    def basic_skill(self):
        ...


class Printer(OfficeEquipment):
    def what_i_can_do(self):
        print('Я умею печатать')

    @staticmethod
    def moving_to_warehouse(quantity=0):
        try:
            if not quantity.isdigit():
                print('Количество должно являтся числом')
                return None
        except AttributeError as err:
            quantity = 0
        OfficeEquipmentWarehouse.moving_to_warehouse('Printer', quantity)


    @staticmethod
    def basic_skill():
        print('Бжжжщщ', end='')
        for i in range(10):
            print('.', end='')
            sleep(0.3)
        print('Лист напечатан!')




class Scanner(OfficeEquipment):
    def what_i_can_do(self):
        print('Я умею сканировать')

    @staticmethod
    def moving_to_warehouse(quantity=0):
        try:
            if not quantity.isdigit():
                print('Количество должно являтся числом')
                return None
        except AttributeError as err:
            quantity = 0
        OfficeEquipmentWarehouse.moving_to_warehouse('Scanner', quantity)

    @staticmethod
    def basic_skill():
        print('Бжжжщщ', end='')
        for i in range(10):
            print('.', end='')
            sleep(0.3)
        print('Лист отсканирован!')


class Xerox(OfficeEquipment):
    def what_i_can_do(self):
        print('Я умею делать копии')

    @staticmethod
    def moving_to_warehouse(quantity=0):
        try:
            if not quantity.isdigit():
                print('Количество должно являтся числом')
                return None
        except AttributeError as err:
            quantity = 0
        OfficeEquipmentWarehouse.moving_to_warehouse('Xerox', quantity)

    @staticmethod
    def basic_skill():
        print('Бжжжщщ', end='')
        for i in range(10):
            print('.', end='')
            sleep(0.3)
        print('Копия сделана!')


Xerox.moving_to_warehouse()