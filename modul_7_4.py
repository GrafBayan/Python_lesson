team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
name_1 = 'Мастера кода'
name_2 = 'Волшебники Данных'
challenge_result = ''


print('В команде %s участников: %s !' % (name_1, team1_num))
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print('Команда {} решила задач: {} ! '.format(name_2, score_2))
print('{} решили задачи за {} с !'.format(name_2, round(team2_time, 1)))
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Победа команды {name_1}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Победа команды {name_2}!'
else:
    challenge_result = 'Ничья!'

print(challenge_result)
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по'
      f' {round((team1_time + team2_time)/(score_1 + score_2), 1)} секунды на задачу!')