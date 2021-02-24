'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

with open('exersise_hw_2.txt', 'r') as file:
    #                               Способ через readline()
    str_count = 0
    words_count = 0
    print(f'\n{"*" * 50}\nВариант с помощью .readline():\n')
    while True:
        l1 = file.readline()
        if l1 == '':
            break
        if ' ' in l1:
            words_count = len(l1.split())
        else:
            words_count = 1
        print(f'Строка № {str_count + 1} кол-во слов {words_count}: {l1}', end='')
        str_count += 1
    print(f'\nКоличество строк: {str_count}\n{"*" * 50}')

    #                               Способ через readlines()
    print(f'Вариант с помощью .readlines():\n')
    # Ставим курсор вначало
    file.seek(0)
    l2 = file.readlines()
    words_count = 0
    for k, v in enumerate(l2):
        if ' ' in v:
            words_count = len(v.split())
        else:
            words_count = 1
        print(f'Строка № {k + 1} кол-во слов {words_count}: {v}', end='')
    print(f'\nКоличество строк: {k + 1}\n{"*" * 50}')
