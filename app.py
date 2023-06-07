from flask import Flask
from routes.projects import projects
from flask_cors import CORS
import os
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app)

load_dotenv()
DB_URI = os.getenv('DB_URI')

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(projects)