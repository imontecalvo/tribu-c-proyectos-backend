from app import app
from utils.db import db
import os

with app.app_context():
    db.init_app(app)
    db.create_all()

PORT = os.getenv('PORT')

if __name__ == '__main__':
    app.run(port=PORT, debug=True)