import asyncio
import random


sentences = [
    "шлет всем большой привет",
    "справился с упражнением",
    "научился слать данные по TCP",
    "отправил текст успешно",
    "просто мастер Python!",
    "будет вести следующую лекцию"
]


class EchoServerProtocol(asyncio.Protocol):

    def __init__(self):
        super(EchoServerProtocol, self).__init__()
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        response = '%s %s' % (message, random.choice(sentences))
        print(response)
        self.transport.write(response.encode())
        self.transport.close()


loop = asyncio.get_event_loop()

# Each client connection will create a new protocol instance
coro = loop.create_server(EchoServerProtocol, '0.0.0.0', 9999)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
