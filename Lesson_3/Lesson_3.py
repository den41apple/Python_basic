'''dry - do not repeat yourself Не повторяй ебя если что то собираешься скопировать - создай функцию
для многократного использования.
'''
y = 1
get = 4
def line(x): #  Помни про вложенные функции
    y = 3
    def inner(a):
        nonlocal y #    Обращается к переменной в функцию уровнем выше
        y = 3 * x + 1 #     Здесь будет ошибка, так как глобальная переменная доступна только на чтение
        a = 2
        global get  #   Обращается к глобальной функции

        print(f'a{a}')
        print(y)
    inner(x)


print(y)
l = line  # В переменную можно записать функцию
print(l(2)) # return отвечает за вывод информацию
l(2) #  Ее теперь можно вызывать как функцию
print(y)

def my_shiny_func(a: int, b: int) -> float: # Аннтация типов чисто косметическая вещь, она ни на что ни влияет
    return a / b
print(my_shiny_func(b=1, a=2))  # Задание параметров не по порядку

#   А что если м ыне знаем сколько аргументов пойдет в функцию?
def func(*args):  #  *args - функция будет принимать все в КОРТЕЖ. args - все договорились, достаточно только *
    print(args)
func(1, 2, 3, 4, 5, 6, 7)

def func_2(*l):  #  args - все договорились, достаточно только * и что то нgitаписать
    print(l)
    print(max(l))

def func_3(*args, **kwargs): #  **kwargs будет словариком
    print(kwargs)

dict_3 = {'k': 2, 'left': func}
func_3(1, 2, 3, 4, 5, 6, 7, k=2) # kwargs служит для того что бы прокинуть дополнительные аргументы не обьявленные по ключу

print(divmod(5, 2))  # Принимает два числа и возвращает кортеж 2-х чисел. Целое от деления и остаток
print(abs(-5.2))  # Модуль
print(round(5.7828723, 2))  # Округление. Первым аргументом идет число, вторым кол-во знаков после запятой
print(pow(5, 2))  # Возведение первого числа во вторую
print(max(5, 2))
print(min(5, 2))
# print(sum(5, 2))