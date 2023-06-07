from utils.db import db    
from models.project import Project

def add_project(project):
    db.session.add(project)
    db.session.commit()

def get_all_projects():
    return Project.query.all()

def delete_project(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()

def update_project(id, data):
    project = Project.query.get(id)
    project.name = data['name']
    project.cost = data['cost']
    project.created_at = data['created_at']
    db.session.commit()