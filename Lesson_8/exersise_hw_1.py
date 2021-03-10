'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class Date:
    month_dic = {
        'Января': '01',
        'Февраля': '02',
        'Марта': '03',
        'Апреля': '04',
        'Мая': '05',
        'Июня': '06',
        'Июля': '07',
        'Августа': '08',
        'Сентября': '09',
        'Октября': '10',
        'Ноября': '11',
        'Декабря': '12'
    }

    def __init__(self, date: str):
        self.__class__.date = date
        self.extract(date)

    @classmethod
    def extract(cls, date):
        month = 0
        for i in Date.month_dic:
            if date.find(i) != -1:
                month = Date.month_dic[i]
                break
            else:
                month = '13'
        date_int = int(str(date[:2] + month + date[-4:]))
        return cls.validation(date_int)

    @staticmethod
    def validation(date: int):
        if 1 <= int(str(date)[:2]) <= 31 and 1 <= int(str(date)[2:4]) <= 12 and 1 <= int(str(date)[4:]):
            print('Дата верна')
        else:
            print('Дата НЕ верна')


test_date = Date('25-Мая-2020')
