immutable_var = (21, 'Tiamat', 'a' in 'age', [1, 2, 'plug'])
print(immutable_var)
immutable_var[-1][-1] = 3
print(immutable_var)

mutable_list = ['anime', 'gay' in 'gaymer', 1000 - 7, ('tuple in the list', 1)]
mutable_list[0:1] = ['The art']
mutable_list[1:2] = ['Сondemn']
print(mutable_list)