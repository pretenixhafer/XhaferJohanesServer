import io
from contextlib import redirect_stdout
from hello import __main__


def test_hello_prints():
    buf = io.StringIO()
    with redirect_stdout(buf):
        __main__.main()
    assert "Hello" in buf.getvalue()
