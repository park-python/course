"""
Клиент для чат-сервера.
"""
import threading
import socket


HOST = "127.0.0.1"
PORT = 9999


def handle_client_input(sock):
    while True:
        try:
            data = input()
        except KeyboardInterrupt:
            sock.close()
            return

        try:
            sock.send(data.encode("utf-8"))
        except IOError:
            return


def main():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((HOST, PORT))

    threading.Thread(
        target=handle_client_input,
        args=[client_sock], daemon=True
    ).start()

    while True:
        data = client_sock.recv(4096)
        if not data:
            break
        print(data.decode())

    client_sock.close()


if __name__ == '__main__':
    main()
