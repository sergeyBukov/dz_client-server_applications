"""3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе."""

words_list = ["attribute", "класс", "функция", "type"]
for el in words_list:
    try:
        print('Слово записано в байтовом типе:', eval(f'b"{el}"'))
    except SyntaxError:
        print(
            f'Невозможно записать в байтовом типе cлово: "{el}"')
