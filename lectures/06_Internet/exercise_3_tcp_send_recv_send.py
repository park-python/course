import asyncio
import random


sentences = [
    "справился с упражнением",
    "мастер сетевых протоколов!",
    "просто мастер Python!",
    "будет вести следующую лекцию"
]


class EchoServerProtocol(asyncio.Protocol):

    def __init__(self):
        super(EchoServerProtocol, self).__init__()
        self.transport = None
        self.name = None
        self.secret_number = None

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        message = data.decode()

        if self.name is None:
            self.name = message
            self.secret_number = random.randrange(0, 10000000)
            self.transport.write(str(self.secret_number).encode())
            print('%s подключился' % (self.name,))
        else:
            if str(self.secret_number) == message:
                response = 'Yeah! %s %s' % (self.name, random.choice(sentences))
                print(response)
            else:
                response = 'Fail! %s не угадал число: было %s, а пришло %s' % (
                    self.name, self.secret_number, message
                )
                print(response)

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
