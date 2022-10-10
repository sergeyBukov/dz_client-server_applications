# Функции сервера:
# принимает сообщение клиента;
# формирует ответ клиенту;
# отправляет ответ клиенту;
# имеет параметры командной строки:
# -p <port> - TCP-порт для работы (по умолчанию использует порт 7777);
# -a <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
from socket import socket, AF_INET, SOCK_STREAM

SERV_SOCK = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
SERV_SOCK.bind(('localhost', 7777))  # Присваивает порт 7777
SERV_SOCK.listen(5)  # Переходит в режим ожидания запросов
# одновременно обслуживает не более 5 запросов
try:
    while True:
        CLIENT_SOCK, ADDR = SERV_SOCK.accept()  # Принять запрос на соединение
        print("Получен запрос на соединение от %s" % str(ADDR))
        DATA = CLIENT_SOCK.recv(4096)
        print(f"Сообщение: {DATA.decode('utf-8')} было отправлено клиентом: {ADDR}")
        MSG = 'Привет клиент'
        CLIENT_SOCK.send(MSG.encode('utf-8'))
        SERV_SOCK.close()
finally:
    SERV_SOCK.close()
