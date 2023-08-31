from flask import Blueprint, request, jsonify
from models.task import Task
from services import task_service
from services import projects_service
from routes.projects import projects

tasks = Blueprint("tasks", __name__, url_prefix="/tasks")


@tasks.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE, PATCH")
    return response


@projects.route(
    "/<int:project_id>/tasks/<int:task_id>", methods=["GET"], strict_slashes=False
)
def get_a_task_data(project_id, task_id):
    if not projects_service.project_exists(project_id):
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
        return response

    task = task_service.get_task(task_id, project_id)

    if task:
        response = jsonify({"ok": True, "msg": task.to_dict()})
        response.status_code = 200
    else:
        response = jsonify({"ok": False, "msg": "The task does not exist"})
        response.status_code = 404
    return response


@projects.route("/<int:project_id>/tasks/", methods=["POST"], strict_slashes=False)
def new_task(project_id):
    data = request.json
    res = check_fields_new_task(data)
    if res:
        return res

    project = projects_service.project_exists(project_id)
    if not project:
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
        return response

    task = Task(data, project)
    task_service.add_task(task)
    projects_service.update_last_task(project_id)

    response = jsonify({"ok": True, "msg": task.to_dict()})
    response.status_code = 201
    return response


@projects.route(
    "/<int:project_id>/tasks/<int:task_id>", methods=["PUT"], strict_slashes=False
)
def update_task(project_id, task_id):
    data = request.json
    res = check_fields_update_task(data)
    if res:
        return res

    if not projects_service.project_exists(project_id):
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
        return response

    task = task_service.update_task(task_id, project_id, data)
    if task:
        response = jsonify({"ok": True, "msg": task.to_dict()})
        response.status_code = 200
    else:
        response = jsonify({"ok": False, "msg": "The task does not exist"})
        response.status_code = 404
    return response


@projects.route(
    "/<int:project_id>/tasks/<int:task_id>", methods=["DELETE"], strict_slashes=False
)
def delete_task(project_id, task_id):
    if not projects_service.project_exists(project_id):
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
    elif task_service.delete_task(task_id, project_id):
        response = jsonify(
            {"ok": True, "msg": "The task has been deleted successfully"}
        )
        response.status_code = 200
    else:
        response = jsonify({"ok": False, "msg": "The task does not exist"})
        response.status_code = 404
    return response


@projects.route("/<int:project_id>/tasks", methods=["GET"], strict_slashes=False)
def get_tasks_from_project(project_id):
    if projects_service.project_exists(project_id):
        tasks = task_service.get_all_project_tasks(project_id)
        response = jsonify({"ok": True, "msg": [t.to_dict() for t in tasks]})
        response.status_code = 200
    else:
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
    return response


def check_fields_new_task(data):
    fields = [
        "titulo",
        "descripcion",
        "tiempo_estimado_finalizacion",
        "legajo_responsable",
    ]

    for field in fields:
        if not field in list(data.keys()):
            response = jsonify({"ok": False, "msg": f"Field {field} is missing"})
            response.status_code = 400
            return response

    return None


def check_fields_update_task(data):
    fields = [
        "titulo",
        "descripcion",
        "tiempo_estimado_finalizacion",
        "horas_acumuladas",
        "estado",
        "legajo_responsable",
    ]

    for field in fields:
        if not field in list(data.keys()):
            response = jsonify({"ok": False, "msg": f"Field {field} is missing"})
            response.status_code = 400
            return response

    err_msg = ""

    if data["horas_acumuladas"] < 0:
        err_msg = "horas_acumuladas must be a positive number"

    if data["estado"] < 0 or data["estado"] > 2:
        err_msg = "estado is invalid"

    if err_msg != "":
        response = jsonify({"ok": False, "msg": err_msg})
        response.status_code = 400
        return response
    return None
