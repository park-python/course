"""
Простой TCP echo сервер, работающий с одним клиентом.
"""
import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 9999
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)


conn, addr = s.accept()
print('Connection address:', addr)

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print("received data: {}".format(data.decode("utf-8")))
    conn.send(data)  # echo back

conn.close()
