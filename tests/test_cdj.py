import cdj


BAD_SERVER = 'localhost:10000'
GOOD_SERVER = 'localhost:10001'


@cdj.call(server=GOOD_SERVER)
def foo():
    return 'foo fallback'


@cdj.call(server=BAD_SERVER)
def bar():
    return 'bar fallback'


assert foo() == 'pong'
assert bar() == 'bar fallback'
