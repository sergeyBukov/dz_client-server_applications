"""4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode)."""

words_list = ['разработка', 'администрирование', 'protocol', 'standard']

byte_view = []
for el in words_list:
    el_b = el.encode('utf-8')
    byte_view.append(el_b)
print(f'Байтовое представление: {byte_view}')

string_view = []
for el in byte_view:
    el_str = el.decode('utf-8')
    string_view.append(el_str)
print(f'Строковое представление: {string_view}')
