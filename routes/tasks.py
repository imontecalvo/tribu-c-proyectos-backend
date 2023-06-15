from flask import Blueprint, request, jsonify
from models.task import Task
from services import task_service

tasks = Blueprint("tasks", __name__, url_prefix="/tasks")


@tasks.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE, PATCH")
    return response


@tasks.route("/", methods=["GET"], strict_slashes=False)
def get_tasks_data():
    all_tasks = task_service.get_all_tasks()

    response = jsonify({"ok":True, "msg":[i.to_dict() for i in all_tasks]})
    response.status_code = 200
    return response

@tasks.route("/<int:id>", methods=["GET"], strict_slashes=False)
def get_a_task_data(id):
    task = task_service.get_task(id)

    if task:
        response = jsonify({"ok":True, "msg":task.to_dict()})
        response.status_code = 200
    else:
        response = jsonify({"ok":False, "msg": "The task does not exist"})
        response.status_code = 404
    return response


@tasks.route("/", methods=["POST"], strict_slashes=False)
def new_task():
    data = request.json
    res = check_fields_new_task(data)
    if res:
        return res
    
    task = Task(data)
    task_service.add_task(task)

    response = jsonify({"ok":True, "msg": task.to_dict()})
    response.status_code = 201
    return response


@tasks.route('/<int:id>', methods=['PUT'], strict_slashes=False) #.
def update_task(id):
    data = request.json
    res = check_fields_update_task(data)
    if res:
        return res
    
    task = task_service.update_task(id, data)
    if task:
        response = jsonify({"ok":True,"msg":task.to_dict()})
        response.status_code = 200
    else:
        response = jsonify({"ok":False,"msg":"The task does not exist"})
        response.status_code = 404
    return response


@tasks.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_project(id):
    if task_service.delete_task(id):
        response = jsonify({"ok":True,"msg":"The task has been deleted successfully"})
        response.status_code = 200
    else:
        response = jsonify({"ok":False,"msg":"The task does not exist"})
        response.status_code = 404
    return response


def check_fields_new_task(data):
    fields = [ "id_task", "titulo", "descripcion", "tiempo_estimado_finalizacion", "horas_acumuladas", "estado", "responsable"]

    for field in fields:
        if not field in list(data.keys()):
            response = jsonify({"ok": False, "msg": f"Field {field} is missing"})
            response.status_code = 400
            return response
        
    if data["horas_acumuladas"] > 0:
        response = jsonify({"ok": False, "msg": "horas_acumuladas must be a positive number"})
        response.status_code = 400
        return response
    return None


def check_fields_update_task(data):
    fields = [ "id_task", "titulo", "descripcion", "tiempo_estimado_finalizacion", "horas_acumuladas", "estado", "responsable"]

    for field in fields:
        if not field in list(data.keys()):
            response = jsonify({"ok": False, "msg": f"Field {field} is missing"})
            response.status_code = 400
            return response
    
    err_msg = ""
    if data["horas_acumuladas"] < 0:
        err_msg = "horas_acumuladas must be a positive number"
   
    if data["estado"] != "no iniciada" and data["estado"] != "iniciada" and data["estado"] != "finalizada":
        err_msg = "estado is invalid"
    
    if err_msg != "":
        response = jsonify({"ok": False, "msg": err_msg})
        response.status_code = 400
        return response
    return None