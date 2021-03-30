'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
 name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
 оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage,
                        "bonus": bonus
                        }


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя: {self.surname} {self.name}')

    def get_total_income(self):
        print(f'Доход с учетом премии {self.wage + self.bonus:.2f} руб.')


print()  # Отступ для наглядности отображения
'''Передача данных'''
worker_petrov = Position('Максим', 'Петров', 'Вахтёр', 20_000, 15_000)

'''Проверка значения атрибутов'''
print(f'Имя: {worker_petrov.name}')
print(f'Фамилия: {worker_petrov.surname}')
print(f'Должность: {worker_petrov.position}')
print(f'Оклад: {worker_petrov._income["wage"]} руб.')
print(f'Бонус: {worker_petrov._income["bonus"]} руб.')
print()  # Отступ для наглядности отображения

'''Вызов метода экземпляра'''
worker_petrov.get_full_name()
worker_petrov.get_total_income()
