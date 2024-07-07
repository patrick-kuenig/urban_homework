first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(first_word) - len(second_word)) for (first_word, second_word) in zip(first, second)
                if not len(first_word) == len(second_word))

# second_result = (first[index] == second[index] for index in range(max(len(first), len(second))))
# [False, False, False]
# В задании запрашивается "результат сравнения строк", не сразу понятно, что надо сравнить именно длину строк
second_result = (len(first[index]) == len(second[index]) for index in range(min(len(first), len(second))))
# тут как в описании задания: [False, False, True]

print(list(first_result))
print(list(second_result))