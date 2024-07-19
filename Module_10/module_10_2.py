from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name: str, strength: int):
        super().__init__()
        self.name = name
        self.strength = strength


    def run(self):
        enemies = 100
        days = 0
        print(f"{self.name}, на нас напали!")

        while enemies > 0:
            time.sleep(1)
            days += 1
            enemies -= self.strength
            print(f"{self.name} сражается {days} дней(дня), осталось {enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")

