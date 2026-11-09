import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.request import urlopen
from p6_python_web import Handler

class WebTest(unittest.TestCase):
    def test_http_result(self):
        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with urlopen('http://127.0.0.1:' + str(server.server_port) + '/') as response:
                self.assertIn('<output id="result">5</output>', response.read().decode())
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=3)
