'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.

Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км/ч')

    def go(self):
        self.direction = 'Прямо'
        self.speed = 30
        print(f'Врумм, на машине {self.name} цвета {self.color} '
              f'вы завелись и едите {self.direction} со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Вы остановились, ваша скорость стала {self.speed} км/ч')


    def turn_left(self):
        self.direction = 'Налево'
        print(f'Вы повернули {self.direction}')

    def turn_right(self):
        self.direction = 'Направо'
        print(f'Вы повернули {self.direction}')

    def turn_back(self):
        self.direction = 'Назад'
        print(f'Вы повернули {self.direction}')


class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        if self.speed > self.max_speed:
            print(f'Ваша скорость {self.speed} км/ч, вы превышаете!')
        else:
            Car.show_speed(self)


class SportCar(Car):
    pass


class WorkCar(Car):
    max_speed = 40

    def show_speed(self):
        if self.speed > self.max_speed:
            print(f'Ваша скорость {self.speed} км/ч, вы превышаете!')
        else:
            Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

'''Проверки машины каждого типа'''
print('\n' + '*' * 50)
some_town_car = TownCar(70, 'красный', 'Моя машина')
some_town_car.go()
some_town_car.show_speed()
some_town_car.turn_left()
some_town_car.turn_right()
some_town_car.turn_back()
some_town_car.stop()
print(f'Это машина полицейская: {some_town_car.is_police}')

print('\n' + '*' * 50)
some_sport_car = SportCar(120, 'красный', 'Спортивная машина')
some_sport_car.go()
some_sport_car.show_speed()
some_sport_car.turn_left()
some_sport_car.turn_right()
some_sport_car.turn_back()
some_sport_car.stop()
print(f'Это машина полицейская: {some_sport_car.is_police}')

print('\n' + '*' * 50)
some_work_car = WorkCar(30, 'коричневый', 'Рабочая лошадка')
some_work_car.go()
some_work_car.show_speed()
some_work_car.turn_left()
some_work_car.turn_right()
some_work_car.turn_back()
some_work_car.stop()
print(f'Это машина полицейская: {some_work_car.is_police}')

print('\n' + '*' * 50)
some_police_car = PoliceCar(70, 'синий', 'полицейская машина')
some_police_car.go()
some_police_car.show_speed()
some_police_car.turn_left()
some_police_car.turn_right()
some_police_car.turn_back()
some_police_car.stop()
print(f'Это машина полицейская: {some_police_car.is_police}')
