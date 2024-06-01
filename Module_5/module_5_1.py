class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            print(new_floor)
        else:
            print("Такого этажа не существует")


villa = House('Седьмое небо', 20)
villa.go_to(21)
