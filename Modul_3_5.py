def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        if first * get_multiplied_digits(int(str_number[1:])) == 0:
            return first
        else:
            return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
print(get_multiplied_digits(40203))
print(get_multiplied_digits(9))
print(get_multiplied_digits(10))