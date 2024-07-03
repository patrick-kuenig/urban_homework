class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self._is_valid_vin(vin):
            self._vin = vin
        if self._is_valid_numbers(numbers):
            self._numbers = numbers

    def _is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Неверный тип vin номер", f"{vin_number} of wrong type")
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера", f"{vin_number} "
                                                                         f"too long or too short")
        else:
            return True

    def _is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров", f"{numbers} "
                                                                             f"is wrong type!")
        elif len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера", f"{numbers} has wrong length!")
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message, add_info):
        self.message = message
        self.add_info = add_info


class IncorrectCarNumbers(Exception):
    def __init__(self, message, add_info):
        self.message = message
        self.add_info = add_info


if __name__ == "__main__":
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')
