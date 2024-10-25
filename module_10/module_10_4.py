from random import randint
from threading import Thread
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    def __str__(self):
        return f'Table {self.number} - {self.guest}'


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)
        self.guests = Queue()

    def guest_arrival(self, *guests):  # прибытие гостей
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}.')
            else:
                self.guests.put(guest)
                print(f'{guest.name} в очереди')


    def discuss_guests(self):  # обслужить гостей
        while not self.guests.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.guests.empty() and table.guest is None:
                    next_guest = self.guests.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
            sleep(1)

tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]


guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
