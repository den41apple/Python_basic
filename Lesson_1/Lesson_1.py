#
#                                      1-й урок Основы языка Python
#   @luchanos - телега
#   Дедлайн за 4 часа до урока который через неделю
#   Снижает оценку если сделал меньше половины, но если алгоритм не самый оптимальный - то не снижает
#   Программировани и разработка - это командная игра. Поэтому можно и нужно обсуждать проблемы в коде с другими студентами
#   изучить основы Python - это синтаксис
#   Книга луц, и "глохаем алгоритмы"
#   По Git у него есть на канале видео как пользоваться
#   А так же по тому как его подружить с PyCharm-ом
#   Хорошо бы тренироваться писать код без IDE можно отключить автозамену и подстановку
#   Пишем директорию так: potok_7 Без больших букв, с подчеркиванием пробелов

# Типы:
# str - строка
# int - целое число
# float - число с плавающей точкой
# bytes - байт строка  bs = b'sfgsdfsdfs' это будет байт строкой, когда ставишь Б перед чем то, но можно и bytes писать
# bool - True или False
#   Файл - корректно называть модулем. В ошибки интерпретатор тоже пишет типа ошибка в модуле
#   a, b - Это объекты a + b - это выражение. А a + b == b + a - Это инструкции
#   Деление int / int = float так же при делении если переводить в int - число не округляется, дробная часть просто выкидывается после запятой
#   // - Целочисленное деление. Тип данных int будет.
# print(type(36//6))
#     int % int = int стоит про это помнить
#   int(17.8) = 17 Потому что int просто откидывает часть после запятой
#   132132 % 10 = 2 Потому что остаток от деления это сколько не хватает что бы разделить еще раз на 10
#   2312413413 // 10 - Как метод отсекания последней части либо всей части кроме последнего

# answer = input('Пигрог буш?') #
# if answer == 'да':  # Это называется логический оператор и тип этого выражения bool
#     print('Ем пирожок')
# else:
#  print('Как хош')

#   И вот подобное логическое выражение возращает Tru или False
# print(answer == 'да')
#  Конкатинация - это сложение строк. Самый нубский метод работы со строками. На собеседованиях лучше не показывать это
#  Потому что с точки зрения алгоритма это каждый рад добавление в память потом опять сложение потом добаление в новую ячейку

# Форматирование строк
# nach = input('Введите начинку: ')
# s = 'Это пирожок с начинкой: %s' % nach # s - означает строка. Этот способ хорош потому что ты прописываешь тип и таким образом меньше ошибаешься
# print(s)
# f'{nach:.6f} - округление