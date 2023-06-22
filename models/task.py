from utils.db import db
import datetime as dt


class Task(db.Model):
    id_tarea = db.Column(db.Integer, primary_key=True)
    id_proyecto = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(60))
    descripcion = db.Column(db.String(100))
    tiempo_estimado_finalizacion = db.Column(db.Integer)
    horas_acumuladas = db.Column(db.Integer, default=0)
    estado = db.Column(db.Integer, default=0)
    legajo_responsable = db.Column(db.Integer)

    def __init__(self, data, project):
        self.id_tarea = project.ultima_tarea + 1
        self.id_proyecto = project.codigo
        self.titulo = data["titulo"]
        self.descripcion = data["descripcion"]
        self.tiempo_estimado_finalizacion = data["tiempo_estimado_finalizacion"]
        self.legajo_responsable = data["legajo_responsable"]

    def update_data(self, data):
        self.titulo = data["titulo"]
        self.descripcion = data["descripcion"]
        self.tiempo_estimado_finalizacion = data["tiempo_estimado_finalizacion"]
        self.horas_acumuladas = data["horas_acumuladas"]
        self.estado = data["estado"]
        self.legajo_responsable = data["legajo_responsable"]

    def to_dict(self):
        return {
            "id_proyecto": self.id_proyecto,
            "id_tarea": self.id_tarea,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "tiempo_estimado_finalizacion": self.tiempo_estimado_finalizacion,
            "horas_acumuladas": self.horas_acumuladas,
            "estado": self.estado,
            "legajo_responsable": self.legajo_responsable,
        }
