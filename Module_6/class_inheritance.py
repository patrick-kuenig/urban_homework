class Car:
    price = 1000000
    horse_power = 90

    def horse_powers(self):
        return self.horse_power


class Nissan(Car):
    price = 2000000

    def horse_powers(self):
        return self.horse_power ** 2


class Kia(Car):
    price = 3000000

    def horse_powers(self):
        return self.horse_power ** 3
