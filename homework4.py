immutable_var = tuple([False, 20, "Hello", ["pizza", "donut", "burger", "house"]])
print("Tuple which can't be changed:\n\t{}\n".format(immutable_var))
#immutable_var[0] = True
#Выдаст TypeError, т.к. нельзя обратиться и изменить элемент в кортеже (неизменяемый тип данных)
#Но можно изменить изменяемый тип данных в самом кортеже (например список)

immutable_var[3][3] = "hotdog"
print("Tuple in which a mutable element (list) was changed:\n\t{}\n".format(immutable_var))
# Вывод в консоли:
# (False, 20, 'Hello', ['pizza', 'donut', 'burger', 'house'])
# (False, 20, 'Hello', ['pizza', 'donut', 'burger', 'hotdog'])

mutable_list = ["John", "Mike", False, 2024, ["ice cream", "bag", "bike"]]
mutable_list[1] = ("Bob")
print("List with something changed:\n\t{}\n".format(mutable_list))
mutable_list[4] += mutable_list
print("Self-referencing list, similar to a recursive function without break:\n\t{}".format(mutable_list))
#['John', 'Mike', False, 2024, ['ice cream', 'bag', 'bike', 'John', 'Mike', False, 2024, [...]]]
#Красивый, безконечный список)
