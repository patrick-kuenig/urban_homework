def average_grade(grades, students):
    print(dict(map(lambda x, y: (x, round(sum(y)/len(y), 1)), sorted(students), grades)))
    return


if __name__ == "__main__":
    average_grade([[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]], {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
