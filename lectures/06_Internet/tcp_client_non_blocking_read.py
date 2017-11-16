"""
Показываем, что такое select. Запускать в связке с tcp_server_periodic_send.py
"""
import select
import socket

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect(("127.0.0.1", 9999))

sock1.setblocking(0)

#sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock2.connect(("127.0.0.1", 10000))
#sock2.setblocking(0)

#sockets = {
#    sock1.fileno(): sock1,
#    sock2.fileno(): sock2
#}

while True:
    result = select.select([sock1.fileno()], [], [])
    print(result)
    data = sock1.recv(1024)
    if not data:
        print("connection closed")
        break
    print(data)

