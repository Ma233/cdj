import socket
from StringIO import StringIO

END = '\r\n\r\n'


def pack(data):
    return ''.join([str(data), END])


def call(server):

    def deco(f):

        def _f(*args, **kwargs):
            recv_data = StringIO()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                s.connect(server)
            except socket.error:
                s.close()
                return f(*args, **kwargs)

            try:
                s.sendall(pack(f.func_name))
                while True:
                    data = s.recv(16)
                    if data:
                        recv_data.write(data)
                    else:
                        break
            finally:
                s.close()

            return recv_data.getvalue()

        return _f

    return deco
