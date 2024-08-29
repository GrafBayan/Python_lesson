import io
from pprint import pprint
test = [
'Text for tell.',
'Используйте кодировку utf-8.',
'Because there are 2 languages!',
'Спасибо!'
]

def custom_write(file_name, strings):
    tuple_ = []
    a = 0
    for i in strings:
        a += 1
        file = open(file_name, 'a', encoding='utf-8')
        tuple_.append((a, file.tell()))
        file.write(f'{i}\n')
        file.close()
    string_position = dict(zip(tuple_, strings))
    return string_position

result = custom_write('test_file.txt', test)
for elem in result.items():
  print(elem)