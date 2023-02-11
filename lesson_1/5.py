"""Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице."""

import subprocess
import chardet

args = ['ping', 'yandex.ru']

yandex_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for i in yandex_ping.stdout:
    result = chardet.detect(i)
    str_type = i.decode(result['encoding']).encode('utf-8')
    print(str_type.decode('utf-8'))