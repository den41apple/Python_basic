# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


#   Создаем список со всеми типами данных
# NoneType, числа, Исключения, Строки, байты, множества, списки, кортежи, словари
main_list = [None, 'string', b'bytes', set(), [1, '2'], ('cortage'), {'Слово': 'word'}]


for i in range(len(main_list)):
    print(type(main_list[i]))