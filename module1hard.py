grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dict_result = dict()
control = sorted(students)
for num in grades:
    dict_result[control[grades.index(num)]] = sum(num)/len(num)
print(dict_result)
Name = input('Введите имя ученика, для вывода его средней оценки: ')
print(dict_result[Name])