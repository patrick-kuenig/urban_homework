class Vehicle:
    _COLOR_VARIANT = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = color

    def get_model(self):
        return f'Модель: {self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def get_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self._COLOR_VARIANT:
            self._color = new_color
            return f'Цвет машины изменен на: {new_color}'
        else:
            return f"Машина не может быть покражена в {new_color}"


class Sedan(Vehicle):
    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)
        self.__PASSENGER_LIMIT = 5


if __name__ == "__main__":
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
    vehicle1.get_info()
    print(vehicle1.set_color('Pink'))
    print(vehicle1.set_color('BLACK'))
    vehicle1.owner = 'Vasyok'
    vehicle1.get_info()
