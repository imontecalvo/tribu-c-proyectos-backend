from utils.db import db    
from models.task import Task

def add_task(task):
    db.session.add(task)
    db.session.commit()

def get_all_tasks():
    return Task.query.all()

def get_all_project_tasks(project_id):
    return Task.query.filter_by(id_project = project_id)

def get_task(id):
    return Task.query.get(id)

def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return True
    False

def update_task(id, data):
    task = Task.query.get(id)
    if task:
        task.update_data(data)
        db.session.commit()
        return task
    return False