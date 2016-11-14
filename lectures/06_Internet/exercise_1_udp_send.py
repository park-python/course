import asyncio
import random


sentences = [
    "шлет всем большой привет",
    "справился с упражнением",
    "научился слать данные по UDP",
    "отправил текст успешно",
    "просто мастер Python!",
    "будет вести следующую лекцию"
]


class EchoServerProtocol:

    def __init__(self):
        super(EchoServerProtocol, self).__init__()
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        response = '%s %s' % (message, random.choice(sentences))
        print(response)
        self.transport.sendto(response.encode(), addr)


def main():
    loop = asyncio.get_event_loop()
    print("Starting UDP server on 0.0.0.0:9999")

    # One protocol instance will be created to serve all client requests
    listen = loop.create_datagram_endpoint(
        EchoServerProtocol,
        local_addr=('0.0.0.0', 9999)
    )

    transport, protocol = loop.run_until_complete(listen)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    transport.close()
    loop.close()


if __name__ == "__main__":
    main()
