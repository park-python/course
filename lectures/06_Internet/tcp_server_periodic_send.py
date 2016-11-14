"""
TCP сервер, который работает с одним клиентом и отправляет данные в сокет
раз в интервал времени. Нужен, чтобы показать работу select на стороне клиента.
"""
import socket
from datetime import datetime
import time


TCP_IP = '127.0.0.1'
TCP_PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Connection address:', addr)
    while True:
        time.sleep(5)
        try:
            conn.send(str(datetime.now()).encode("utf-8"))
        except IOError:
            break

    print('Connection closed:', addr)
    conn.close()
