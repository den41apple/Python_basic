'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randint

with open('exersise_hw_5.txt', 'w') as file:
    for i in range(10):
        file.writelines(str(f'{randint(1, 100)} '))

with open('exersise_hw_5.txt', 'r') as file:
    l1 = (file.readline()).split()
    for i in range(len(l1)):
        l1[i] = int(l1[i])
    print(f'Числа: {l1}')
    print(f'Сумма чисел в файле: {sum(l1)}')
