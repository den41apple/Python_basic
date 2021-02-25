'''
                                          ПОЛЕЗНЫЕ ИНСТРУМЕНТЫ
'''

#           import
# time, random, sys, os, collections, abc, re, subprocess, copy
#

'''Время работы программы'''
# from datetime import datetime
# from time import sleep
#
# start = datetime.now()
# sleep(3)
# print(f'Start working at: {start}')
# finish = datetime.now()
# print(f'Finish at: {finish}. Working time: {finish - start}')
#

'''Случайные числа'''
# from random import random, randint, randrange
# print(random())
# print(randint(1, 20))
# print(randrange(1, 10, 2))

'''Прокидывание параметров в функцию'''
# from sys import argv
#
# def send_emails(*args, **kwargs):
#     for email in args:
#         print(f'Письмо на почту {email} отправлено')
#
# # если запуск из модуля
# send_emails('lol@mail.ru', 'asda@mail.ru')
# send_emails(*argv[1:]) # хватает из консоли, ток нужно начинать со второго элемента
# # send_emails(**'dsf')


'''Генераторы списков'''
# Есть то что до for а есть после, он из двух частей
# Слева то что делаем с элементом, а справа как мы его выбираем
# l = [el for el in range(11) if el % 2 == 0]    # List comprehension
# print(l)
# s = {el for el in range(11) if el % 2 == 0}
# print(s)
# t = (el for el in range(11) if el % 2 == 0)  # а вот с tuple почему то генерируемый обьект получается
# print(t)
# t = tuple(el for el in range(11) if el % 2 == 0)  # а вот с tuple поправили
# print(t)
#
# # Для словариков
# dic = {k: v for k, v in enumerate(range(10))} # итерация сразу по двум элементам
# print(dic)
# dic = {k: k for k in range(10)}
# print(dic)
#
# l1 = [(1, 'test'), (2, 'some'), (3, 'blabla')]
# print({k: v for k, v in l1})   #  РАССМОТРЕТЬ ТАКУЮ КОНСРУКЦИЮ, КАКИЕ ДАННЫЕ ПРИХОДЯТ В ПЕРЕМЕННЫХ ПРИ ИТЕРИРОВАНЫЕ
# # КАК Я ПОНЯЛ ТАКАЯ ШТУКА ПРИНИМАЕТ ПОЗИЦИОННО КОРТЕЖ


'''Импорт файлов'''
# from file import function
# #   КОГДА ИМПОРТИРУЕМ ФУНКЦИЮ, ВЫПОЛНЯЕТСЯ  ЕЩЕ И КОД ИМПОРТИРУЕМОГО МОДУЛЯ, ЧТОБ ЭТОГО ИЗБЕЖАТЬ:
# if __name__ == '__main__':

'''НАСТОЯЩИЕ ПОЛНОЦЕННЫЕ ГЕНЕРАТОРЫ'''
# print(list((x for x in range(10))))
# l = [x for x in range(100_000_000)]  # Для красоты можно писать 000_000
# Генератор - частный случай генератора
def my_range(a):
    print('start')
    cnt = 0
    while cnt < a:
        yield cnt # Подразумевает  что возвращает обьект генератора и не завершает функцию в отличии от return
        cnt += 1

a = my_range(100)
for el in a:
    print(el)
#
# next(a) # передаем generator object
# next(a) # а второй продолжает раоту после yield


'''FUNCTOOLS'''
# from functools import reduce
# def f(a):
#     return str(a) * 10
#
# def summa(a, b):
#     return a + b
# def filter_a(a):
#     if a < 5:
#         return str(a) * 10
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = reduce(summa, a) # функцию, а на второй параметр коллекцию. Он распечатывает ТОЛЬКО ПО ДВА ЭЛЕМЕНТА,
# # ПО ЭТОМУ ФУНКЦИЯ ИТЕРИРУЕМАЯ ДОЛЖНА ПРИНИМАТЬ НА ВХОД ДВА ЭЛЕМЕНТА
# print(res)
#
# print(list(map(f, a)))
#
# print(list(filter(filter_a, a)))

# for x in cycle(a): # это бегущая строка
#     print(x)
# from functools import count, cycle
# for x in count():
#     print(x)
#
# from functools import partial
#
# def summa(*args, x=2, y=3):
#     ag = x + y
#     print(args)
#     return ag
#
# l1 = partial(summa(43), '1', '2')



# # Для получения точности при дробных числах
# from decimal import Decimal
#
# print((Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) - Decimal('0.3'))


#
# # Считать количество ссылок на обьект
#
# from sys import getrefcount
#
# print(getrefcount(a))

