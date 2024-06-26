my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
while n < len(my_list):
    i = my_list[n]
    if i > 0:
        print(i)
        n += 1
    elif i == 0:
        n += 1
    else:
        break