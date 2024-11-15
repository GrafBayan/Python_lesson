def add_everything_up(a, b):
    con = a + b
    return con


try:
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))


except TypeError:
    def add_everything_up(a, b):
        con = str(a) + str(b)
        return con


    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))

else:
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
    print("Никаких строчек, только числа")