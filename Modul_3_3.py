def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(c = [1, 2, 3])
print_params(b = 25)

values_list = [2, 'value', True]
values_dict = {'a': 3, 'b': 'str', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Sam', [1, 2, 3]]
print_params(*values_list_2, 42)