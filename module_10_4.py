from threading import Thread
from random import randint
from queue import Queue


class Table:

    def __int__(self, number):
        self.number = number
        self.guest = None

    def __repr__(self):
        return f'{self.number}'


class Guest(Thread):

    def __int__(self, name):
        self.name = name

    def run(self):
        pass


class Cafe:

    def __init__(self, *tables):
        self.tables = [*tables]
        self.queue = Queue()

    def guest_arrival(self, *guests):
        pass

    def discuss_guests(self):
        pass


