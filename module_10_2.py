from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.power = power
        self.name = name
    def run(self):
        warrior = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while warrior >= self.power:
            day += 1
            warrior -= self.power
            sleep(1)
            print(f'{self.name} сражается {day} день(дня)..,осталось {warrior} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
sleep(1)
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
