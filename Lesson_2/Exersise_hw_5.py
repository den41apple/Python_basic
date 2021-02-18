# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
#     Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#     Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#     Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#     Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#     Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rank = [7, 5, 6, 6, 8, 3, 3, 2, 2]
print(f'\nНаш список: \n{rank}\n')
#   Попросим пользователя ввести число
number = int(input('Введите число: '))

for i in range(len(rank)):
    # Ставим ограничитель для индекса
    if (i + 1) == len(rank):
        break
    # Проверяем соседние значения
    elif rank[i] == rank[i + 1]:
        # Если число совпадает, добавляем на позицию после двух совпадающих
        if number == rank[i + 1]:
            rank.insert(i + 2, number)
            break
print(f'\nНаш список после обработки: \n{rank}')