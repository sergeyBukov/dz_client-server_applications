"""2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с
информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для
этого:
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
(item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
должна предусматривать запись данных в виде словаря в файл orders.json. При
записи данных указать величину отступа в 4 пробельных символа;
b. Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра"""

import json


def write_order_to_json(item, quantity, price, buyer, date):

    with open('orders.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data)

    with open('orders.json', 'w', encoding='utf-8') as file_write:
        order_list = data["orders"]
        order_info = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
        order_list.append(order_info)
        json.dump(data, file_write, indent=4, ensure_ascii=False)


write_order_to_json('рюкзак', '20', '1000', 'Иван Иванович', '09.10.22')
write_order_to_json('куртка', '65', '65000', 'Иван Иванович', '09.10.22')
write_order_to_json('футболка', '100', '800', 'Иван Иванович', '09.10.22')
