from tah.cli import hello_msg as msg
# import tah.cli.hello_msg as msg

def test_hello():
    m = msg()
    assert m == "hello"
