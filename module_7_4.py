# Использование %:
team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s!'% team1_num)
print('Итого сегодня в командах участников: %s и %s!'%(team1_num,team2_num))

# Использование format():
score_2 = 42
team1_time = 18015.2
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за: {}c!'.format(team1_time))

# Использование f-строк:
score_1 = 40
score_2 = 42
challenge_result = 'победа команды Мастера кода!'
tasks_total = 82
time_avg = 350.4
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %:
print('В команде Мастера кода участников: %s!'% team1_num)
print('Итого сегодня в командах участников: %s и %s!'%(team1_num,team2_num))
print('Команда Волшебники данных решила задач: %s!'% score_2)
print('Волшебники данных решили задачи за: %sc!'% team1_time)
print('Команды решили %s и %s задач.'%(score_1, score_2))
print('Результат битвы: %s'% challenge_result)
print('Сегодня было решено %s задач, в среднем по %s секунды на задачу!'%(tasks_total,time_avg))

# Использование format():
print('В команде Мастера кода участников: {}!'.format(team1_num))
print('Итого сегодня в командах участников: {} и {}!'.format(team1_num,team2_num))
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за: {}c!'.format(team1_time))
print('Команды решили {} и {} задач.'.format(score_1, score_2))
print('Результат битвы: {}'.format(challenge_result))
print('Сегодня было решено {} задач, в среднем по {} секунды на задачу!'.format(tasks_total,time_avg))

# Использование f-строк:
print(f'В команде Мастера кода участников: {team1_num}!')
print(f'Итого сегодня в командах участников: {team1_num} и {team2_num}!')
print(f'Команда Волшебники данных решила задач: {score2}!')
print(f'Волшебники данных решили задачи за: {team1_time}!')
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
