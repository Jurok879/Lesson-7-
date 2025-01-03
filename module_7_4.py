# использование %:

team1_num = 5
team2_num = 6

print("\nВ команде Мастера кода участников: %s !" % team1_num)
print("В команде Волшебники данных участников: %s !" % team2_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num), '\n')

# использование format():

score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451

print("Команда Мастера кода решила задач: {} !".format(score1))
print("Команда Волшебники данных решила задач: {} !".format(score2))
print("Мастера кода решили задачи за {} с !".format(team1_time))
print("Волшебники данных решили задачи за {} с !".format(team2_time), '\n')

# использование f-строк:

tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print(f"Команды решили {score1} и {score2} задачи.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!\n")

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')
