import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.power_of_enemy = 100
        self.days = 0
    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.power_of_enemy > 0:
            time.sleep(1)
            self.days += 1
            self.power_of_enemy -= self.power
            if self.power_of_enemy < 0:
                self.power_of_enemy = 0
            print(f'{self.name} сражается {self.days}... Осталось {self.power_of_enemy} войнов '
                  f'врага.')
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Битвы окончены.")