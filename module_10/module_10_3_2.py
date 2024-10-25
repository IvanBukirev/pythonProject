
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
            print(f'Пополнение {i}: {replenishment}. Баланс: {self.balance}')
            if self.balance>=500 and self.lock.locked():
                self.lock.release()
                print('разблокирован в deposit')

            print(f'заблокирован в начислении {Thread.name}' if self.lock.locked() else f'не заблокирован в начислении {Thread.name}')
            sleep(0.001)


    def take(self):
        for i in range(100):
            withdrawal=randint(50, 500)
            print(f'Запрос{i} на {withdrawal}')
            if withdrawal>self.balance:
                print(f'Запрос {i} отклонён, недостаточно средств')
                self.lock.acquire()
                thr=self.lock.acquire()
                print(f'заблокирован в take')
            else:
                self.balance -= withdrawal
                print(f'Снятие {i}: {withdrawal}. Баланс: {self.balance}.')
            print(f'заблокирован в выдаче {Thread.name}' if self.lock.locked() else f'{Thread.name} не заблокирован в выдаче')
            sleep(0.001)



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')