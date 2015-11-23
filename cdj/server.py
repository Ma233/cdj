import socket
import logging
from StringIO import StringIO

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('cdjumper')
END = '\r\n\r\n'


class SocketServer(object):
    def __init__(self):
        self.soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self, address, listen=1):
        logger.info('Server starting up on %s:%s...', *address)
        self.soket.bind(address)
        self.soket.listen(listen)

        while True:
            connection, client_address = self.soket.accept()
            try:
                recv_data = self.recv(connection)
                logger.info('Recv (%s) from %s', recv_data[:-4], client_address)
                self.response(connection, recv_data)
            finally:
                connection.close()

    def recv(self, connection):
        recv_data = StringIO()

        while True:
            data = connection.recv(16)
            if data:
                recv_data.write(data)
            else:
                break

            # End of a comunicate
            if recv_data.getvalue()[-4:] == END:
                break

        return recv_data.getvalue()

    def response(self, connection, recv_data):
        connection.sendall('pong')


def serve():
    HOST = socket.gethostname()
    SERVER = (HOST, 10001)
    SocketServer().run(SERVER)


if __name__ == '__name__':
    serve()
