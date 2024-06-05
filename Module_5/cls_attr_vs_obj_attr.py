class Building:
    total = 0

    def __init__(self):
        self.total += 1


i = 0
while i < 40:
    _class = Building()

print(Building.total)