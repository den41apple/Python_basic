# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#   Предложим выбрать вариант программы
decision = int(input('Если хотите через list введите "1", через dict "2": '))

#   Попросим ввести месяц
month = int(input('Введите номер месяца от 1 до 12: '))

#   Напишем через list, Все месяца будут по порядку
month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
              'Декабрь']
if decision == 1:
    print(f'Месяц: {month_list[month - 1]}')

#   Напишем через dict, Все месяца будут доступны по ключам
month_dict = {1: 'Январь',
              2: 'Февраль',
              3: 'Март',
              4: 'Апрель',
              5: 'Май',
              6: 'Июнь',
              7: 'Июль',
              8: 'Август',
              9: 'Сентябрь',
              10: 'Октябрь',
              11: 'Ноябрь',
              12: 'Декабрь'
              }
if decision == 2:
    print(f'Месяц: {month_dict[month]}')
