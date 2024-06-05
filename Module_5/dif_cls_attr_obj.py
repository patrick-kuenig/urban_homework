class Building:
	total = 0

	def __init__(self):
		Building.total += 1

	def __str__(self):
		return str(Building.total)

for i in range(40):
	objs = Building()
	print(objs)