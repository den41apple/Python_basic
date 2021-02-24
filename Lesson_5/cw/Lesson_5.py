'''
                                РАБОТА С ФАЙЛАМИ
'''

from io import TextIOWrapper

# l = ["Первая строка\n", "Вторая строка\n", "Третья строка\n"]


# f_o = open('my_shiny_file.txt', 'w', encoding='UTF-8')
# f_o = open('my_shiny_file.txt', 'a', encoding='UTF-8')  # открываем на ДОЗАПИСЬ
# print(f_o)

# #  Без цикла зиписывалась только 1-я строка
# for el in l:
#     f_o.write(el)

# l = ["Первая строка", "Вторая строка", "Третья строка"]
# f_o = open('my_shiny_file.txt', 'r', encoding='UTF-8')
# f_o.writelines(l)       #  ТОЧНО ТАК ЖЕ КАК ЦИКЛ for отработает

# print(f_o.read())
# print(f_o.readlines())

# res = f_o.readline()

# print(f_o.seek(1))  # перевод курсора в файле


# for el in f_o:
#     print(el, end='')

''' Менеджер контекста '''
# with open('my_shiny_file.txt', 'r', encoding='UTF-8') as e:  # менеджер контекста это ТОЛЬКО слово with, а так же и его методы __enter__ и __exit__
#     pass
# print('asd')

''' Классы '''
# class MyPirozhok:
#     def __enter__(self):
#         print('Начинаю работу с пирожком в менеджере контекста')
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Заканчиваю работу с пирожком в менеджере контекста ')
#
# pirozhok = MyPirozhok()  #  Собираем пирожок по рецепту
#
# print('Начало работы')
# with pirozhok:
#     print('Работаю')
#     raise ZeroDivisionError
#
# print('Конец')

# print(f_o.closed) #  Проверка на закрытие

# f_o = open('sample.pdf', 'rb') # PDF - двоичный файл
# print(f_o.read())

# f_o = open('my_shiny_file.txt', 'w', encoding='UTF-8')
# print('sdfdtrghdf55', file=f_o)

# import json
# #
# # # получаем данные из json
# with open("json_example.json", "r") as json_obj:
#     data = json.load(json_obj)
#     print(data)
#     print(type(data))
#     # some_data = {"user_id": 123123,
#     #              "position": "devloper",
#     #              "city": "Moscow",
#     #              "l": [1, 2, 3, {"fd": 123}]
#     #              }
#     # s = json.dump(some_data, json_obj)  #  Записывает, ДАМПИТ в json
#     # print(s)