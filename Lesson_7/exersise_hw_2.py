'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import abstractmethod


class Clothes:
    @abstractmethod
    def calculate_fabric_volume(self):
        pass

    def __init__(self, v=0, h=0):
        self.v = v
        self.h = h


'''Пальто'''


class Coat(Clothes):

    @property
    def calculate_fabric_volume(self):
        return self.v / 6.5 + 0.5


'''Костюм'''


class Suit(Clothes):

    @property
    def calculate_fabric_volume(self):
        return 2 * self.h * 3


coat_for_casual = Coat(v=70)
suit_forwork = Suit(h=1.8)

print(f'Для прогулочного пальто требуется {coat_for_casual.calculate_fabric_volume:.2f} метров ткани')
print(f'Для рабочего костюма требуется метров ткани: {suit_forwork.calculate_fabric_volume:.2f} метров ткани')