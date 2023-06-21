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
    "/<int:id_project>/tasks/<int:id_task>", methods=["GET"], strict_slashes=False
)
def get_a_task_data(id_project, id_task):
    if not projects_service.project_exists(id_project):
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
        return response

    task = task_service.get_task(id_task, id_project)

    if task:
        response = jsonify({"ok": True, "msg": task.to_dict()})
        response.status_code = 200
    else:
        response = jsonify({"ok": False, "msg": "The task does not exist"})
        response.status_code = 404
    return response


@projects.route("/<int:id_project>/tasks/", methods=["POST"], strict_slashes=False)
def new_task(id_project):
    # Chequeamos que los campos de la request sean correctos
    data = request.json
    res = check_fields_new_task(data)
    if res:
        return res

    project = projects_service.project_exists(id_project)
    if not project:
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
        return response

    task = Task(data, project)
    task_service.add_task(task)
    projects_service.update_last_task(id_project)

    response = jsonify({"ok": True, "msg": task.to_dict()})
    response.status_code = 201
    return response


@projects.route(
    "/<int:id_project>/tasks/<int:id_task>", methods=["PUT"], strict_slashes=False
)
def update_task(id_project, id_task):
    # Chequeamos que los campos de la request sean correctos
    data = request.json
    res = check_fields_update_task(data)
    if res:
        return res

    if not projects_service.project_exists(id_project):
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
        return response

    task = task_service.update_task(id_task, id_project, data)
    if task:
        response = jsonify({"ok": True, "msg": task.to_dict()})
        response.status_code = 200
    else:
        response = jsonify({"ok": False, "msg": "The task does not exist"})
        response.status_code = 404
    return response


@projects.route(
    "/<int:id_project>/tasks/<int:id_task>", methods=["DELETE"], strict_slashes=False
)
def delete_task(id_project, id_task):
    if not projects_service.project_exists(id_project):
        response = jsonify({"ok": False, "msg": "The project does not exist"})
        response.status_code = 404
    elif task_service.delete_task(id_task, id_project):
        response = jsonify(
            {"ok": True, "msg": "The task has been deleted successfully"}
        )
        response.status_code = 200
    else:
        response = jsonify({"ok": False, "msg": "The task does not exist"})
        response.status_code = 404
    return response


@projects.route("/<int:id>/tasks", methods=["GET"], strict_slashes=False)
def get_tasks_from_project(id):
    if projects_service.project_exists(id):
        tasks = task_service.get_all_project_tasks(id)
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
        "responsable",
    ]

    for field in fields:
        if not field in list(data.keys()):
            response = jsonify({"ok": False, "msg": f"Field {field} is missing"})
            response.status_code = 400
            return response

    return None


def check_fields_update_task(data):
    fields = [
        "id_tarea",
        "id_proyecto",
        "titulo",
        "descripcion",
        "tiempo_estimado_finalizacion",
        "horas_acumuladas",
        "estado",
        "responsable",
    ]

    for field in fields:
        if not field in list(data.keys()):
            response = jsonify({"ok": False, "msg": f"Field {field} is missing"})
            response.status_code = 400
            return response

    err_msg = ""

    if data["horas_acumuladas"] < 0:
        err_msg = "horas_acumuladas must be a positive number"

    if (data["estado"] < 0 or data["estado"] > 2):
        err_msg = "estado is invalid"

    if err_msg != "":
        response = jsonify({"ok": False, "msg": err_msg})
        response.status_code = 400
        return response
    return None
