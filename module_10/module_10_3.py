
from random import randint
from threading import Thread,Lock
from time import sleep




class Bank:
    def __init__(self):
        self.balance = 0
        self.lock =  Lock()

    def deposit(self):
        for i in range(100):
            replenishment=randint(50, 500)
            self.balance+=replenishment
            print(f'Пополнение: {replenishment}. Баланс: {self.balance}')
            if self.balance>=500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)


    def take(self):
        for i in range(100):
            withdrawal=randint(50, 500)
            print(f'Запрос на {withdrawal}')
            if withdrawal>self.balance:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            else:
                self.balance -= withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}.')
            sleep(0.001)



bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')