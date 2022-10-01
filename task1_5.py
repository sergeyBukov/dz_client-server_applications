"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице."""

import subprocess

args1 = ['ping', 'yandex.ru']
args2 = ['ping', 'youtube.com']

subproc_ping = subprocess.Popen(args1, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line.decode('utf-8'), end='')

subproc_ping = subprocess.Popen(args2, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line.decode('utf-8'), end='')
