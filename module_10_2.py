from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int) -> None:
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        days = 0
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            self.enemy -= self.power
            sleep(1)
            days += 1
            print(f'{self.name} сражается {
                  days} день(дня)..., осталось {self.enemy} войнов ')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
third_knight = Knight('Sir Tristan', 5)
knights: list = [first_knight, second_knight, third_knight]

[x.start() for x in knights]
[x.join() for x in knights]
print('Все битвы закончились!')
