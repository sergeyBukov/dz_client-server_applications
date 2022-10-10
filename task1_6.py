"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое."""

from chardet import detect

# Создаем файл
file = open('test_file.txt', 'w', encoding='utf-8')
file.write('сетевое программирование\n')
file.write('сокет\n')
file.write('декоратор\n')
file.close()

# Узнаем кодировку
with open('test_file.txt', 'rb') as file:
    content = file.read()
encoding = detect(content)['encoding']
print('encoding: ', encoding)

# Открываем файл в известной кодировке
with open("test_file.txt", encoding=encoding) as file:
    for line in file:
        print(line, end='')
