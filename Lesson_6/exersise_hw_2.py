'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.

Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

class Road:
    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self.thickness = thickness
    def calc_mass(self):
        mass = self._length * self._width * 25 * self.thickness
        print(f'\nДля укладки дороги длинной {self._length} метров шириной {self._width} метров, '
              f'\nи толщиной {self.thickness} сантиметров потребуется {mass / 1000:.0f} тонн асфальта')

m5_road = Road(2000, 20, 6)
m5_road.calc_mass()