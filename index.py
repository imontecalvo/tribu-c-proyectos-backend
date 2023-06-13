from app import app
from utils.db import db
import os
from gevent.pywsgi import WSGIServer

with app.app_context():
    db.init_app(app)
    db.create_all()

PORT = os.getenv('PORT')

if __name__ == '__main__':
    http_server = WSGIServer(('', int(PORT)), app)
    http_server.serve_forever()