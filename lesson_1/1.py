"""Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных."""

words = ['разработка', 'сокет', 'декоратор']

for i in words:
    print(f'содержание: {i}, тип:{type(i)}')

words_2 = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
           '\u0441\u043e\u043a\u0435\u0442',
           '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for i in words_2:
    print(f'содержание: {i}, тип:{type(i)}')