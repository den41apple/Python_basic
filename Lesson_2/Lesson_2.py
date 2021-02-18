#   ВСТРОЕННЫЕ ТИПЫ ДАННЫХ Python:
#   NoneType, числа, Исключения, Строки, байты, множества, списки, кортежи, словари
#   После урока обязательно проработать то что есть в файле

#   Побитовые операции они делают вычисление в двоичной системе и потом обратно переводят
#   Логические операторы можно посмотреть в файле
# print(5 | 9) #  будет 13

#   Перевод системы счисления
# print(int(bin(8), 2))
# print(bin(88)) # Префикс 0b означает что мы работаем в двоичной системе
# print(hex(14))  #   16-иричная система счисления и тут префикс 0x
# print(oct(14))  #   8-иричная система счисления Префикс 0o

# #   Побитовый сдвиг - означает что все разряды двигают влево это _1101 -> 11010
# print(int('0100', 2))
# print(int('01000', 2))
#   Прочитать книгу код, можно что бы разобраться
# print(13>>5) #  Это как раз сдвиг >> или <<

# #   Типы данных БАЙТЫ Т BYTEARRAY
# print(chr(123), chr(1), chr(200)) #   Берем символ из таблицы ASCII, это указан номер порядковый в таблице
# print(ord('{'), ord('e'), ord('a')) # Обратная операция, возвращает порядковый номер символа
# print('123' > 'sdfd')   #   А строки тоже можно сравнивать, сравнивается по таблице ASCII
#
# s = 'first' + 'second'
# print(s[0]) # Первый элемент строки

#   Срезы
'''
Общая формула среза [start:finish:step]
'''
# s = '0123456789'
# print(s[::4]) # Выводит с шагом 4


# #   Быстрый реверс
# print(s[-1])
# print(s[::-2]) #    Отрицательный шаг говорит показывай четный порядок но выводи НАОБОРОТ
# print(s[::-1]) #    А таким образом можно выводить строку в обратном порядке)))
# print(reversed(s))

# #   Цикл FOR для обхода последовательностей
# for x in reversed(s):
#     print(x)
#     print(s)
#     print(x * 10)
#     print('Вы великолепны')
#
#
# d = 'dsd SOme STsRIng'
# for x in d[3::2].lower(): # а тут даже можно дописать метод, полноценное логическое выражение
#     print(x)
#     print(x * 10)
#     print('Вы великолепны')

# print(d.split('s'))
# c = 'd', 'd SOme ST', 'RIng'
# print(','.join(c))

#   КОЛЛЕКЦИИЮ СПИСКИ - изменяемые

# l1 = [False, 2, 3, 4, 5]
# l2 = [True, False]
# l3 = ['t', 'e', 's', 't']
# print('t' in l3)
# print('t' in 'testetets') # оператор in позволяет проверять что-то
# print(l3.count('t'))
#
# l4 = [l1, l2, l3]
# print(l4)
#
# print(l2)
# l2.insert(1, 'some value') # Функция inserst ставит что то туда куда скажешь синктаксис inserst(индекс, что положить)
# print(l2)
# l2.pop()
# print(l2)


#   Задача замена местами

# a = 1
# b = 2
# print(a, b)
# a, b = b, a # кстати питон воспринимает это как кортеж параметров
# print(a, b)
#
# l = [1, 2, 3, 4]
# l[2], l[3] = l[3], l[2]
# print(l)

#   МНОЖЕСТВА - ИЗМЕНЯЕМЫЙ, НЕУПОРЯДОЧЕННЫЙ, УНИКАЛЬНЫЙ, считает по хешу, значит сравниваются только неизменяемые
#   скобки как у словаря но пустое множество нельзя задать просто скобками!!!
s = {}
print(type(s))
s = set()
print(type(s))

#

a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set(a))
print(tuple(set(a))) #  Tuple - это тип кортеж

some_dict = { 'name': { 'name': 'Nikolai',
              'surname': 'Silnykh',
              'position': 'developer'},
              'surname': 'Silnykh',
              'position': 'developer'

}

print(some_dict['name'])

story_stone = {         #   Такой словарь можно использовать вместо if
    'left': 'leftik',
    'right': 'dfgs',
    'straight': 'ssdfg'
}
print(story_stone.get('lef')) # возвратить если нет  ключа который записываем СИНТАКСИС  get(key, default, value)

print(print(a))


#   Тернарный оператор
result = 123 if a == 3 else 5 # он нужен чисто для красоты кода


