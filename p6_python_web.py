import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

def p6_web_add(left, right):
    return left + right  # P6_PYTHON_WEB_BUG

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/':
            self.send_error(404)
            return
        value = p6_web_add(2, 3)
        body = ('<!doctype html><html><head><title>P6 Python Web</title></head>'
                '<body><h1>P6 Python Web</h1><output id="result">'
                + str(value) + '</output></body></html>').encode()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *_):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8080)
    args = parser.parse_args()
    ThreadingHTTPServer(('0.0.0.0', args.port), Handler).serve_forever()
