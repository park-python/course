import threading
import socket


HOST = "127.0.0.1"
PORT = 9999

SEP = b"\0"


def handle_client_input(sock):
    while True:
        try:
            data = input()
        except KeyboardInterrupt:
            sock.close()
            return

        try:
            sock.send(data.encode("utf-8") + SEP)
        except IOError:
            return


def main():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((HOST, PORT))

    threading.Thread(
        target=handle_client_input,
        args=[client_sock], daemon=True
    ).start()

    accumulated_data = bytes()

    while True:
        data = client_sock.recv(1)
        if not data:
            break

        accumulated_data += data

        # show how accumulated_data grows.
        # print(accumulated_data)

        messages = []

        while True:
            if SEP in accumulated_data:
                msg, rest = accumulated_data.split(SEP, 1)
                accumulated_data = rest
                messages.append(msg)
            else:
                break

        for message in messages:
            print(message.decode())

    client_sock.close()


if __name__ == '__main__':
    main()
