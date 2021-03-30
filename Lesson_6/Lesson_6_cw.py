'''
                            ОБЪЕКТИВНО ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ (ООП)
'''

# Генератор - это тоже часть ООП
from random import randint

# Классы пишутся в CamelCase, и с большой буквы
class Auto:
    # ПОЛЕ ЭКЗЕМПЛЯРА - это то что жестко закрепленно в чертеже (Обращение как Auto.material)
    material = 'steel'  # Если мы меняем это поле где то внутри методов оно поменяется ДЛЯ ВСЕХ
    secret_model_id = 12345

    # __init__ - Это инициализатор, но в паре с методом __new__ - они конструктор объекта
    def __init__(self, color, engine_power):
        self.color = color              # self.еще что то задается только в ините
        self.engine_power = engine_power
        self.is_on = False          # Как вариант установки дефлотного значения
        self.material = 'glass'  #  Это будет ПОЛЕ ЭКЗЕМПЛЯРА, это не поле экземпляра но то что в __init__ оно ищется в первую очередь
        # self.secret_number = randint(100_000_000)

    def gas(self):
        print(f'Auto with color{self.color} an engine power '
              f'{self.engine_power} make Wruuuuummm')

    def switch_on(self):
        if self.is_on:
            print('Auto has been on switched on yet')
            return  # Чтоб не шел дальше по коду включать двигатель
        self.is_on = True
color = 'red'
# my_shiny_auto = Auto(color, 100) # Это конкретный ЭКЗЕМПЛЯР

# Если мы хотим обратиться к методу мы вызываем ЭКЗЕМПЛЯР.метод()
# my_shiny_auto.gas()
# print(my_shiny_auto.is_on)
# my_shiny_auto.is_on()
# print(my_shiny_auto.is_on)
# print(my_shiny_auto.material)

# print(my_shiny_auto.secret_number, my_shiny_auto.secret_model_id)

#               МОДИФИКАТОРЫ ДОСТУПА
# self.auto - Публичный
# self._auto - Защищенный
# self.__auto - Приватный

#           НАСЛЕДОВАНИЕ

class WarAuto(Auto):
    def __init__(self, color, engine_power): # Если переписать какие то поля надо сначала родительские, потом метода
            # А сдесь в дочернем надо сделать вот так:
        super().__init__(color, engine_power)
    def shoot(self):
        print('Fire!!!')
    def gas(self):
        print('I make noise by my machine gun')
war_car = WarAuto('red', 100)
war_car.material # Мы можем обращаться к классу к тем же методам родительскам класса
war_car.shoot()
war_car.gas()


