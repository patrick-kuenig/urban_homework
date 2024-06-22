team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
challenge_result = 'Мастера кода'
tasks_total = 82
time_avg = 350.4

# % formatting
print("В команде Мастера кода участников %d!" % team1_num)
print("Итого сегодня в командах участников: %d и %d!" % (team1_num, team2_num))

# .format method
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {} с!".format(team1_time))

# f-strings
print(f"Команды решили {team1_num} и {score_2} задачю")
print(f"Результат битвы: победа команды {challenge_result}!")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")
