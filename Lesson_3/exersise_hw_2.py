'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''


def func_about(name, surname, year, city, email, phone):
    '''Предположил что одной строкой должен быть написан код выводящий данные о пользователе, а сам вывод можно в несколько'''
    return f'Данные о пользователе:\nИмя: {name}\nФамилия: {surname}\nГод рождения: {year}\nГород проживания: {city}\ne-mail: {email}\nТелефон: {phone}'


print(func_about(name='Андрей',
           surname='Сильных',
           year='1993',
           city='г. Нижний Тагил',
           email='den41@bk.ru',
           phone='+7(985)973-16-73'
           ))

