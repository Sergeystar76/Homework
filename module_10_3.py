import random
import threading
from time import sleep

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rand_d = random.randint(50, 500)
            self.balance += rand_d
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {rand_d}. Баланс: {self.balance}.')
            sleep((0.001))
    def take(self):
        for y in range(100):
            rand_t = random.randint(50, 500)
            if self.balance >= rand_t:
                self.balance -= rand_t
                print(f'Снятие: {rand_t}. Баланс: {self.balance}.')
                sleep(0.001)

            else:
                print(f'Запрос отклонён, недостаточно средств')
                sleep(0.001)
                self.lock.acquire()
            
bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')