import threading
from time import sleep
from random import randint


class Bank:

    def __init__(self):
        self.balance = 500
        self.lock = threading.Lock()
        self.thread_count = 100

    def deposit(self):
        for _ in range(self.thread_count):
            self.random_choise = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                self.balance += self.random_choise
                print(f'Пополнение: {
                      self.random_choise}. Баланс: {self.balance}')
            else:
                self.balance += self.random_choise
                print(f'Пополнение: {
                      self.random_choise}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(self.thread_count):
            self.random_choise = randint(50, 500)
            print(f'Запрос на {self.random_choise}')
            if self.random_choise <= self.balance:
                self.balance -= self.random_choise
                print(f'Снятие: {self.random_choise}. Баланс{self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
