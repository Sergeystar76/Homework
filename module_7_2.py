import io
from pprint import pprint
strings = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
file_name = 'test.txt'
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    number = 0
    new_dict = {}
    for item in strings:
        pos = file.tell()
        file.write(f"{item}\n")
        number += 1
        new_dict[number, pos] = item
    return new_dict
    file.close()




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)