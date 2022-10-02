"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице."""

import subprocess
import chardet
import platform

param = '-n' if platform.system().lower() == 'windows' else '-c'
args1 = ['ping', param, '2', 'yandex.ru']

subproc_ping = subprocess.Popen(args1, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
