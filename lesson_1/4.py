"""Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode)."""

words = ['разработка', 'администрирование', 'protocol', 'standard']

for i in words:
    byte_view= i.encode('utf_8')
    print(byte_view)
    str_view= byte_view.decode('utf-8')
    print(str_view)