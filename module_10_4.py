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
        sleep(randint(1, 2))


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
            print(f'Очередь: {self.queue.qsize()}, занятые столы: {
                  len([value for value in self.tables.values() if value != None])}')
            if self.queue.empty() and all(value for value in self.tables.values()):
                break
            else:
                for tab_number, tab_guest in self.tables.items():
                    if tab_guest is not None:
                        tab_guest.join()
                        if tab_guest.is_alive() == False:
                            print(
                                f'{tab_guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {tab_number} свободен')
                            self.tables[tab_number] = None
                            break
                    elif tab_guest is None:
                        self.tables[tab_number] = self.queue.get()
                        print(
                            f'{self.tables[tab_number].name} вышел из очереди и сел(-а) за стол номер {tab_number}')
                        self.tables[tab_number].start()


if __name__ == '__main__':

    tables = [Table(number) for number in range(1, 6)]

    guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya',
                    'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

    # guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman']
    guests = [Guest(name) for name in guests_names]

    cafe = Cafe(*tables)

    cafe.guest_arrival(*guests)

    cafe.discuss_guests()
