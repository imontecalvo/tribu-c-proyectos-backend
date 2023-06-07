from flask import Blueprint, request, jsonify
from models.project import Project
from services import projects_service

projects = Blueprint('projects', __name__, url_prefix='/projects')


@projects.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE, PATCH')
    return response


@projects.route('/', methods=['GET'], strict_slashes=False)
def get_projects_data():
    all_projects = projects_service.get_all_projects()

    response = jsonify([i.to_dict() for i in all_projects])
    response.status_code = 200
    return response


@projects.route('/', methods=['POST'], strict_slashes=False)
def new_projects():
    name = request.json["name"]
    cost = request.json["cost"]
    project = Project(name, cost)

    projects_service.add_project(project)

    response = jsonify(project.to_dict())
    response.status_code = 201
    return response


@projects.route('/<int:id>', methods=['PUT'], strict_slashes=False)
def update_project(id):
    projects_service.update_project(id, request.json)

    response = jsonify({"status":"ok","msg":"The project has been updated successfully"})
    response.status_code = 200
    return response


@projects.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_project(id):
    projects_service.delete_project(id)

    response = jsonify({"status":"ok","msg":"The project has been deleted successfully"})
    response.status_code = 200
    return response

