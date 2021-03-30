'''
ПОЛЕЗНЫЕ ДОПОЛНЕНИЯ:
Статические методы и методы класса
'''

# Декоратор @staticmethod метода класса такой метод вызывается напрямую через имя класса
# Благодаря ему это убудт разные имена в ячейках памяти, не будут друг друга перезаписывать

#
# class User:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#     @staticmethod
#     def class_info(self):
#         print('Hello')
#
#     def get_full_name(self):
#         return f'{self.name} {self.surname}'
#     @classmethod
#     def create_info_attr(cls):
#         cls.info = 'INFORMATION'
#
#
# User.class_info()

'''Создание собственных исключений'''

# class MyError(Exception):
#     def __init__(self):
#         self.txt = txt
#
# def connect():
#     pass
#
# def get_friends():
#     # data = ['tom', 'kate']
#     try:
#         if not data:
#             raise MyError('Список друзей пуст')
#         for i in data:
#
#             print(i)
#     except MyError as e:
#         print(e)
#
# def start_bot():
#     connect()
#     get_friends()


''' PIP этот система управления пакетами'''
# pip install prettytable
# pip install -r reuirements.txt


'''Установка вирутальной среды'''
# На каждый пайтон идут свои зависимости
# pip install virtualvenv

'''psutil - получает инфу о железе компа'''

'''requests - использует веб разработчики, позволяет получать данные с интернета'''

'''Урок со Свиридовым'''
# Генератор случайных itcyflwfnbhbxys[ чисел
from uuid import uuid4
from abc import ABC, abstractmethod
from requests import request





class Ticket(ABC):
    def __init__(self):
        self.vaild = True
        self.ticket_id = uuid4()

    # Теперь метод надо будет обязательно реализовать в дочерних, и его аргументы тоже обязательны
    @abstractmethod
    def use_me(self):
        pass

    @abstractmethod
    def annul(self, *args, **kwargs):
        pass

    @abstractmethod
    def notify_host(self, *args, **kwargs):
        pass

    def show_info(self):
        return {'valid': self.vaild, 'ticket_id': self.ticket_id}


    @staticmethod # Просто функция внутри класса НЕПРИВЯЗАННАЯ которую можно вызывать независимо от экземпляра и класса
    def some_func(a, b, c):
        print('Вывожу информацию о истории возникновения билетов')



''' Еще вариант пометить класс как асбтрактный'''


class TeaterTicketAbstract(Ticket, ABC):
    e - mail: str
    send_email_client: EmailClient


class EmailClient:
    def __init__(self, email):
        self.email = email

    def send_email(self):
        print('Отправил письмо')

    def __call__(self, *args, **kwargs):
        self.send_email()


class TeaterTicket(TeaterTicketAbstract):
    e_mail = 'some-emial@lolkekcheburek.com'
    send_email_client = EmailClient(e_mail)

    def use_me(self):
        self.vaild = False
        print('Даем человеку бинокль в подарок')

    # А это метод ЭКЗЕМПЛЯРА
    def annul(self, reason):
        self.vaild = False
        print(f'Билет id {self.ticket_id} был аннулирован по причине {reason}')
        # Вот так можно обращаться к классу экземпляра потому что он носит в себе класс
        self.__class__.notify_host()

    # Делает НЕ ПРИВЯЗАННЫМ к экземпляру, и вместо self будет cls это уже метод КЛАССА
    @classmethod
    def notify_host(cls, data):
        print(f'Отправляю POST запрос с дынными {data} на адрес почты {cls.e_mail}')
        cls.send_email_client()


class TeaterTicketBranch(TeaterTicketAbstract):
    e_mail = 'another-emaill@mail.com'  ''' таким образом cls уже будет новый лкасс, и поле cls.e_mail уже будет этого класса
                                            если мы используем @classmethod в родительском классе'''
    send_email_client = EmailClient(e_mail)


class FlightTicket(Ticket):
    url = 'http://air-trololo.com'

    def use_me(self):
        self.vaild = False
        print('Даем человеку маску в подарок')

    def annul(self, reason):
        self.vaild = False
        print(f'Билет id {self.ticket_id} был аннулирован по причине {reason}')

    # Делает НЕ ПРИВЯЗАННЫМ к экземпляру, и вместо self будет cls
    @classmethod
    def notify_host(cls, data):
        print(f'Отправляю POST запрос с дынными {data} на адрес {cls.url}')


class Controller:

    def __init__(self, controller_id):
        self.controller_id = controller_id

    def _use_ticket(self, ticket: Ticket):
        ticket.use_me()
        print(f'Контролеер id {self.controller_id} осуществил погашение билета {ticket.ticket_id}')

    def _annul_ticket(self, ticket: Ticket, reason: str):
        ticket.annul(reason)
        print(f'Контролеер id {self.controller_id} осуществил аннулирование билета {ticket.ticket_id}')

    def business_logic(self, event, ticket):
        if event == 'событие_1':
            self._use_ticket(ticket)
        elif event == 'событие_2':
            self._annul_ticket(ticket, 'событие_2')


client = EmailClient('ывпавыа')
client()
# controller = Controller(1)
# t_ticket = TeaterTicket()
# f_ticket = FlightTicket()
#
# t_ticket.notify_host('какиет то данные')
# controller.business_logic('событие_1', f_ticket)
# ticket = Ticket() # Упадет с ошибкой так как на основании абстрактного класса нельзя создавать экземпляры



