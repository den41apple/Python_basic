'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
'''

with open('exersise_hw_7.txt', 'r') as file:
    firms_dic = {}
    average_profit_dic = {}
    average_profit = 0
    average_cnt = 0
    while True:
        l1 = file.readline().split()
        if l1 == []:
            break
        firms_dic[l1[1] + ' ' + l1[0]] = int(l1[2]) - int(l1[3])
        if int(l1[2]) >= int(l1[3]):
            average_profit += int(l1[2]) - int(l1[3])
            average_cnt += 1
    average_profit_dic['average_profit'] = int(average_profit / average_cnt)

import json

with open('exersise_hw_7.json', 'w') as file_js:
    json.dump([firms_dic, average_profit_dic], file_js)
