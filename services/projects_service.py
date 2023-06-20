from utils.db import db
from models.project import Project


def add_project(project):
    db.session.add(project)
    db.session.commit()


def get_all_projects():
    return Project.query.all()


def get_project(id):
    return Project.query.get(id)


def delete_project(id):
    project = Project.query.get(id)
    if project:
        db.session.delete(project)
        db.session.commit()
        return True
    False


def update_project(id, data):
    project = Project.query.get(id)
    if project:
        project.update_data(data)
        db.session.commit()
        return project
    return False


def project_exists(id):
    project = Project.query.get(id)
    if project:
        return True
    return False
