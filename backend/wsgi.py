from wsgiref.simple_server import make_server

from app import app

if __name__ == '__main__':
    server = make_server('', 5000, app)
    server.serve_forever()