'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self):
        self.title = None

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        self.title = 'Ручка'

    def draw(self):
        print(f'{self.title} начала отрисовку')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Карандаш'

    def draw(self):
        print(f'{self.title} начал отрисовку')


class Handle(Stationery):
    def __init__(self):
        self.title = 'Маркер'

    def draw(self):
        print(f'{self.title} начал отрисовку')


'''Проверка метода draw по каждому экземпляру'''
print('\n' + '*' * 50)
some_pen = Pen()
some_pen.draw()

print('\n' + '*' * 50)
some_pencil = Pencil()
some_pencil.draw()

print('\n' + '*' * 50)
some_handle = Handle()
some_handle.draw()
