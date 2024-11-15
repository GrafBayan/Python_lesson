first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
Z = zip(first, second)
first_result = (len(x) - len(y) for x, y in Z if len(x) != len(y))
second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))
print(list(first_result))
print(list(second_result))