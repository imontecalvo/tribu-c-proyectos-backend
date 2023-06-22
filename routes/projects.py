from flask import Blueprint, request, jsonify
from models.project import Project
from models.task import Task
from services import projects_service
from services import task_service

projects = Blueprint("projects", __name__, url_prefix="/projects")


@projects.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE, PATCH")
    return response


@projects.route("/", methods=["GET"], strict_slashes=False)
def get_projects_data():
    all_projects = projects_service.get_all_projects()

    response = jsonify({"ok": True, "msg": [i.to_dict() for i in all_projects]})
    response.status_code = 200
    return response


@projects.route("/<int:id>", methods=["GET"], strict_slashes=False)
def get_a_project_data(id):
    project = projects_service.get_project(id)

    if project:
        response = jsonify({"ok": True, "msg": project.to_dict()})
        response.status_code = 200
    else:
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
    return response


@projects.route("/", methods=["POST"], strict_slashes=False)
def new_projects():
    data = request.json
    res = check_fields_new_project(data)
    if res:
        return res

    project = Project(data)
    projects_service.add_project(project)

    response = jsonify({"ok": True, "msg": project.to_dict()})
    response.status_code = 201
    return response


@projects.route("/<int:id>", methods=["PUT"], strict_slashes=False)  # .
def update_project(id):
    data = request.json
    res = check_fields_update_project(data)
    if res:
        return res

    project = projects_service.update_project(id, data)
    if project:
        response = jsonify({"ok": True, "msg": project.to_dict()})
        response.status_code = 200
    else:
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
    return response


@projects.route("/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete_project(id):
    if projects_service.delete_project(id):
        response = jsonify(
            {"ok": True, "msg": "The project has been deleted successfully"}
        )
        response.status_code = 200
    else:
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
    return response


def check_fields_new_project(data):
    fields = [
        "id_cliente",
        "id_producto",
        "version",
        "customizacion",
        "nombre",
        "costo_estimado",
    ]

    for field in fields:
        if not field in list(data.keys()):
            response = jsonify({"ok": False, "msg": f"Field {field} is missing"})
            response.status_code = 400
            return response

    if data["costo_estimado"] < 0:
        response = jsonify(
            {"ok": False, "msg": "costo_estimado must be a positive number"}
        )
        response.status_code = 400
        return response
    return None


def check_fields_update_project(data):
    fields = [
        "id_cliente",
        "id_producto",
        "version",
        "customizacion",
        "nombre",
        "estado",
        "horas_consumidas",
        "costo_estimado",
    ]

    for field in fields:
        if not field in list(data.keys()):
            response = jsonify({"ok": False, "msg": f"Field {field} is missing"})
            response.status_code = 400
            return response

    err_msg = ""
    if data["costo_estimado"] < 0:
        err_msg = "costo_estimado must be a positive number"
    if data["horas_consumidas"] < 0:
        err_msg = "horas_consumidas must be a positive number"
    if data["estado"] < 0 or data["estado"] > 2:
        err_msg = "estado is invalid"

    if err_msg != "":
        response = jsonify({"ok": False, "msg": err_msg})
        response.status_code = 400
        return response
    return None
