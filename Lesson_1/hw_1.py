#
#   1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
#    и сохраните в переменные, выведите на экран.


# #   Создаю переменные
# a = 1
# b = 2
# print('*'*50)
# print(f'Переменная №1: {a} Переменная №2: {b}')
# print('*'*50, '\n')
#
# #   Запрашиваю у пользователя числа
# print('*'*50)
# a = int(input('Теперь введи переменную №1: '))
# b = int(input('Теперь введи переменную №2: '))
# print('\nМолодец! Твой результат: ')
# print(f'Переменная №1: {a}   Переменная №2: {b}')
# print('*'*50, '\n')
#
# #   Запросим строки
# print('*'*50)
# print('Давай теперь введем строки:\n')
# a = str(input('Теперь введи переменную №1: '))
# b = str(input('Теперь введи переменную №2: '))
# print('\nМолодец! Твои строки: ')
# print(f'Строка №1: {a} \nСтрока №2: {b}')
# print('*'*50, '\n')


# #   2. Пользователь вводит время в секундах.
# #   Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
#
# #   Просим пользователя ввести время в секундах
# seconds_input = int(input('Введи время в секундах: '))
#
# #   Переводим сначала в часы
# hours = seconds_input // 60 // 60
#
# #   Переводим в минуты
# minutes = seconds_input // 60
# while minutes > 60:
#     minutes = minutes - 60
#
# #   Переводим в секунды
# seconds = seconds_input - hours * 60 - minutes * 60
# while seconds > 60:
#     seconds = seconds - 60
#
# #   Выводим на экран в правильном формате
# print(f'Время: {hours:0{2}}:{minutes:0{2}}:{seconds:0{2}}')


# #   3. Узнайте у пользователя число n.
# #   Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
#
# #   Запросим число у пользователя
# print('*' * 50)
# n = int(input('Введите число: '))
#
# #   Для того что бы выполнить конкатинацию переведем это в строку
# n = str(n)
#
# #   Теперь посчитаем результат, выполнив конкатинацию, затем переведем в целые числа и выполним сложение чисел
# result = int(n) + int(n + n) + int(n + n + n)
# print(f'Выполним сложение чисел: {n} + {n + n} + {n + n + n} = {result}')
# print('*' * 50)


# #   4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# #   Для решения используйте цикл while и арифметические операции.
# print('*'*50)
# #   Попросим ввести число
# number = int(input('Введи целое положительное число: '))
#
# # Производим первую операцию которая продолжится в цикле while. Отделаем последнюю цифру и убираем одну цифру из number
# a = number % 10
# number = number // 10
#
# while number > 0:
#     if number % 10 > a:
#         a = number % 10
#     number = number // 10
# print('*' * 50)
# print(f'Максимальная цифра в числе: {a}')
# print('*' * 50)


# #   5. Запросите у пользователя значения выручки и издержек фирмы.
# #   Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# #   или убыток — издержки больше выручки).
# #   Выведите соответствующее сообщение.
# #   Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# #   Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
#
# #   Запрашиваем у пользователя значения выручки и издержек
# print('*' * 50)
# income = float(input('Введите размер выручки руб.: '))
# costs = float(input('Введите размер затрат руб.: '))
# print('*' * 50)
# print('РЕЗУЛЬТАТ:')
#
# #   Определяем фин. результат
# if income > costs:
#     print('Выручка больше издержек')
#     profit = (income - costs) / income
#     print(f'Рентабельность: {profit}')
#     staff_count = int(input('Введите количество сотрудников: '))
#     print(f'Прибыль  на одного сотрудника: {(income - costs) / staff_count:.2f} руб.')
# elif income < costs:
#     print('Издержки больше выручки')
# else:
#     print('Выручка равна затратам')
# print('*' * 50)


# #   6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# #   Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# #   Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# #   Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#
# #   Запросим значения
# print('*' * 50)
# a = float(input('Каков результат спортсмена в 1-й день: '))
# b = float(input('Сколько километров должен пробежать спортсмен: '))
# print('*' * 50)
# #   Введем переменную дня, присвоим еденицу как день начала отсчета
# day = 1
# print('РЕЗУЛЬТАТ:')
# while a < b:
#     a = a + a * 0.1
#     day += 1
#     # Печатаем каждый день результат
#     print(f'{day}-й день: {a:.2f} км.')
# print('*' * 50, f'\nОтвет: на {day}-й день спортсмен достиг результата - не менее {b} км.')
# print('*' * 50)
