from math import sqrt, pi


# вместо искажения имени с __ использую нелокальные аттрибуты _
# кажется более целесообразно
class Figure:
    sides_count = 0

    def __init__(self, sides: list, color: tuple, filled: bool):
        if self.__is_valid_sides(sides):
            self._sides = sides
        if self.__is_valid_color(*color):
            self._color = color
        self.filled = filled

    # использую как getter, "возвращать список RGB цветов" нет особого смысла
    def get_color(self):
        return self._color

    # проверяет, является ли переданный цвет rgb корректным
    @staticmethod
    def __is_valid_color(r, g, b):
        if 255 >= r >= 0 and 255 >= g >= 0 and 255 >= b >= 0:
            return True
        else:
            return False

    # setter для цвета фигуры
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self._color = (r, g, b)
        else:
            return

    # setter для сторон фигуры
    def set_sides(self, sides):
        if Figure.__is_valid_sides(sides):
            self._sides = sides
        else:
            return

    @staticmethod
    def __is_valid_sides(sides):
        if len(sides) == 1 or len(sides) == 3:
            return True
        else:
            return False

    def __len__(self):
        return sum(self._sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)
        self._radius = self._sides[0] / (2*pi)

    def get_square(self):
        return round(pi * (self._sides[0] / (2*pi)) ** 2, 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)
        self.height = 2 * (self.get_square() / self._sides[2])

    def get_square(self):
        a = self._sides[0]
        b = self._sides[1]
        c = self._sides[2]
        s = self.__len__() / 2
        return round(sqrt(s * (s - a) * (s - b) * (s - c)), 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)
        self._sides = [sides[0] for i in range(12)]

    def get_volume(self):
        side = self._sides[0]
        return side ** 3


# тестирование
if __name__ == '__main__':
    triangle = Triangle([3, 4, 5], (255, 0, 0), True)
    print(triangle.get_square())
    print(triangle.get_color())
    triangle.set_color(2, 45, 240)
    print(triangle.get_color())
    print(triangle._sides)
    triangle.set_sides([2, 4, 5])
    print(triangle.get_square())
    print((len(triangle)))
    triangle.set_color(0000, 500, 1000)
    print("Ура, пропускается!")
    print(triangle.get_color())

    circle = Circle([10], (200, 50, 200), False)
    print(circle.get_square())
    print(circle._radius)
    circle.set_sides([2, 3])
    print(circle._sides)
    circle.set_sides([15])
    print(circle._radius)
    print(circle.get_square())

    cube = Cube([2], (0, 0, 0), False)
    print(cube.get_volume())
    print(len(cube))
    cube.set_sides([3])
    print(cube.get_volume())
