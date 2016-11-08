"""
Неблокирующий сервер с Event Loop'ом.
"""
import select
import socket
from collections import deque


HOST = "127.0.0.1"
PORT = 9999
clients = {}


class Client:

    def __init__(self, sock):
        self.sock = sock
        self.deque = deque()


def broadcast(poll, data):
    for client in clients.values():
        client.deque.append(data)
        poll.register(client.sock, select.POLLOUT)


def main():
    listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_sock.bind((HOST, PORT))
    listen_sock.listen(5)

    poll = select.poll()
    poll.register(listen_sock, select.POLLIN)

    while True:

        for fd, event in poll.poll():

            # сокет с ошибкой или соединение было закрыто
            if event & (select.POLLHUP | select.POLLERR | select.POLLNVAL):
                poll.unregister(fd)
                client = clients[fd]
                print('Client {} disconnected'.format(client.sock.getpeername()))
                del clients[fd]

            # слушающий сокет
            elif fd == listen_sock.fileno():
                client_sock, addr = listen_sock.accept()
                client_sock.setblocking(0)
                fd = client_sock.fileno()
                clients[fd] = Client(client_sock)
                poll.register(fd, select.POLLIN)
                print('Connection from {}'.format(addr))

            # новые данные от клиента
            elif event & select.POLLIN:
                client = clients[fd]
                data = client.sock.recv(4096)
                if not data:
                    # на следующей итерации цикла мы получим POLLNVAL
                    # для этого клиента - и удалим его из списка клиентов.
                    client.sock.close()
                    continue

                broadcast(poll, data)

            # сокет клиента готов к записи
            elif event & select.POLLOUT:
                client = clients[fd]
                data = client.deque.popleft()
                sent = client.sock.send(data)
                if sent < len(data):
                    client.deque.appendleft(data[sent:])
                if not client.deque:
                    poll.modify(client.sock, select.POLLIN)


if __name__ == '__main__':
    main()
