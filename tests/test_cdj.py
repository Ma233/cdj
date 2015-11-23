import socket
import cdj

HOST = socket.gethostname()
BAD_SERVER = (HOST, 10000)
GOOD_SERVER = (HOST, 10001)


def test_pong():

    @cdj.call(server=GOOD_SERVER)
    def foo():
        return 'foo fallback'

    assert foo() == 'pong'


def test_fallback():

    @cdj.call(server=BAD_SERVER)
    def bar():
        return 'bar fallback'

    assert bar() == 'bar fallback'
