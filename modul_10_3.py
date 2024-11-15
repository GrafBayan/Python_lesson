import threading
import time
import random

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            plus_ = random.randint(50, 500)
            self.balance += plus_
            print(f'Пополнение: {plus_}. Баланс: {self.balance}')

        if self.balance >= 500 and self.lock.locked():
            self.lock.release()

        time.sleep(0.001)

    def take(self):
        for _ in range(100):
            minus_ = random.randint(50, 500)
            print(f"Запрос на {minus_}")

            if minus_ <= self.balance:
                self.balance -= minus_
                print(f"Снятие: {minus_}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
                print("Поток заблокирован из-за недостатка средств")

        time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
