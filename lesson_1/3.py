"""Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе."""

words = ['attribute', 'класс', 'функция', 'type']

for i in words:
    try:
        byte_string = bytes(i, 'ascii')
        print(f'{i} возможно записать в байтовом типе.')
    except:
        print(f'{i} невозможно записать в байтовом типе.')
