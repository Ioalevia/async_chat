"""Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое."""

words = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as file:
    for word in words:
        file.write(f'{word}\n')
file.close()

with open('test_file.txt', 'r') as file:
    print(f'кодировка 6.txt: {file.encoding}\n')
file.close()

with open('test_file.txt', 'r', encoding='utf-8') as file:
    print('Cодержимое:')
    for word in words:
        print(word)
file.close()