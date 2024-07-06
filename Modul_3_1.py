calls = 0


def coun_calls():
    global calls
    calls += 1


def string_info(string):
    string = len(string), str.upper(string), str.lower(string)
    coun_calls()
    return string


def iscontains(string, list_to_search):
    coun_calls()
    list_to_search = str(list_to_search)
    if string.lower() in list_to_search.lower():
        return True
    else:
        return False


print(string_info('I like music'))
print(string_info('The 4th Hokage was the strongest'))
print(iscontains('Urban', ['Mega', 'Omega', 'UrBAN']))
print(iscontains('soDesKA', ['Soul Eater', 'Dark Souls', 'solar']))
print(calls)
