from threading import Thread
from random import randint
from queue import Queue
from time import sleep


class Table:

    def __init__(self, number: int):
        self.number = number
        self.guest = None

    def __repr__(self):
        return f'{self.number}'


class Guest(Thread):

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:

    def __init__(self, *tables):
        self.tables = {table.number: table.guest for table in tables}
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table_number, table_guest in self.tables.items():
                if table_guest is None:
                    self.tables[table_number] = guest
                    print(
                        f'{guest.name} сел(-а) за стол номер {table_number}')
                    guest.start()
                    break
                elif all(value is not None for value in self.tables.values()):
                    print(f'{guest.name} в очереди')
                    self.queue.put(guest)
                    break

    def discuss_guests(self):
        while True:
            if self.queue.empty() and all(table is None for table in self.tables.values()):
                break

            for table_number, guest in self.tables.items():
                if guest is not None and not guest.is_alive():
                    print(
                        f'{guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {table_number} свободен')
                    self.tables[table_number] = None

                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        self.tables[table_number] = next_guest
                        print(
                            f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table_number}')
                        next_guest.start()


if __name__ == '__main__':

    tables = [Table(number) for number in range(1, 6)]

    guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya',
                    'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

    # guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman']
    guests = [Guest(name) for name in guests_names]

    cafe = Cafe(*tables)

    cafe.guest_arrival(*guests)

    cafe.discuss_guests()
