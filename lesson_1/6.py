"""Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое."""

from chardet import detect

words = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as file:
    for word in words:
        file.write(f'{word}\n')
file.close()

with open('test_file.txt', 'rb') as file:
    content = file.read()
encoding = detect(content)['encoding']
print(f'кодировка 6.txt: {encoding}\n')
file.close()

with open('test_file.txt', 'r', encoding=encoding) as file:
    print('Cодержимое:')
    content = file.read()
    print(content)
file.close()