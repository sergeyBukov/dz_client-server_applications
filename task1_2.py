"""2. Каждое из слов «class», «function», «method» записать в байтовом типе без
преобразования впоследовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных"""

words_list = ["class", "function", "method"]

for el in words_list:
    el = eval(f'b"{el}"')
    print(f'{type(el)} + {el} + {len(el)}')

# for el in words_list:
#     el = bytes(el, 'utf-8')
#     print(f'{type(el)} + {el} + {len(el)}')