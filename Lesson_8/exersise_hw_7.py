'''
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров.

Проверьте корректность полученного результата.
'''


# class ComplexNumber:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         print(f'Сумма равна: ')
#         return f'{self.x + other.x} + {self.y + other.y} * i'
#
#     def __mul__(self, other):
#         print(f'Произведение равно: ')
#         return f'{self.x * other.x - (self.y * other.y)} + {self.y * other.x} * i'
#
#
# num_1 = ComplexNumber(1, -2)
# num_2 = ComplexNumber(3, 4)
#
# print(num_1 + num_2)
# print(num_1 * num_2)

_storage = {'Printer': 1,
                'Scanner': 2,
                'Xerox': 0
                }
capasity = 0
for i in _storage.keys():
    capasity += _storage[i]

print(capasity)