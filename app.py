from flask import Flask, jsonify, render_template, send_from_directory
from routes.projects import *
from routes.tasks import *
from flask_cors import CORS
import os
import yaml
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="swagger/templates")
CORS(app)

load_dotenv()
DB_URI = os.getenv("DB_URI")

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(projects)
app.register_blueprint(tasks)


@app.route("/api/swagger.json")
def create_swagger_spec():
    # If you need to edit the API Docs, modify the following .yaml file
    with open("swagger/static/swagger-proyectos.yaml", "r") as stream:
        try:
            spec = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return jsonify(spec)


@app.route("/docs")
@app.route("/docs/<path:path>")
def swagger_docs(path=None):
    if not path or path == "index.html":
        return render_template("index.html", base_url="/docs")
    else:
        return send_from_directory("./swagger/static", secure_filename(path))
