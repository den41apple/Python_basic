'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('exersise_hw_3.txt', 'r') as file:
    cnt = 0
    average_salary = 0
    while True:
        l1 = file.readline()
        if l1 == '':
            break
        l1 = l1.split()
        l1.remove('-')
        if int(l1[1]) < 20:
            print(l1[0])
        average_salary += int(l1[1])
        cnt += 1
    average_salary = average_salary / cnt
    print(f'Средний оклад {average_salary:.3f} тыс. руб. ')
