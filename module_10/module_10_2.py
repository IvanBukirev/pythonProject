
from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f"{self.name}, на нас напали!")
        power_enemy =100
        count_knight = 0
        while power_enemy>0:
            count_knight += 1
            power_enemy -= self.power
            print(f"{self.name}  сражается {count_knight} день(дня)..., осталось {power_enemy if power_enemy>0 else 0} воинов.")
            sleep(1)
        print(f"{self.name} одержал победу спустя {count_knight} дней(дня)!")


first_knight = Knight('Sir Lancelot', 35)
second_knight = Knight("Sir Galahad", 17)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились')