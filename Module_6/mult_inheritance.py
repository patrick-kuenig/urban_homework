class Vehicle:
    def __init__(self):
        self.vehicle_type = 'none'


class Car:
    def __init__(self, horse_power, price=1000000):
        self.price = price
        self.horse_power = horse_power

    def horse_powers(self):
        return self.horse_power


class Nissan(Vehicle, Car):

    def __init__(self, price, horse_power, vehicle_type):
        Car.__init__(self, price, horse_power)
        self.vehicle_type = vehicle_type

    def horse_powers(self):
        return self.horse_power ** 1.5


nissan = Nissan(200, 2000000, 'car')
print(f'Horse powers of this monster: {round(nissan.horse_powers(), 1)}')
print(f'The car costs: {nissan.price}')
