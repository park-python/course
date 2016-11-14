"""
Показываем, что такое select. Запускать в связке с tcp_server_periodic_send.py
"""
import select
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9999))

s.setblocking(0)
s.fileno()

while True:
    result = select.select([s.fileno()], [], [])
    print(result)
    data = s.recv(1024)
    print(data)
