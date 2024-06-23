my_dict = {'Naruto': 720, 'Blich': 347, 'One Piece': 1108}
print(my_dict)
print(my_dict['One Piece'])
my_dict.update({'MGA': 138,
                'Magic battle': 39})
The_best = my_dict.pop('One Piece')
print(The_best)
print(my_dict)

my_set = {'Bread', 1, 3, 0, 1, 'Ge' in 'Geg', 1}
print(my_set)
my_set.update({'Ok Google',
              15})
print(my_set.remove(0))
print(my_set)