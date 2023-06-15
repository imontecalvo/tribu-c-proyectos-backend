from utils.db import db
import datetime as dt


class Task(db.Model):
    
    id_task = db.Column(db.Integer,primary_key=True)
    titulo = db.Column(db.String(60))
    descripcion = db.Column(db.String(100))
    tiempo_estimado_finalizacion = db.Column(db.DateTime())
    horas_acumuladas = db.Column(db.Integer, default=0)
    estado = db.Column(db.String(20), default="iniciada")
    responsable = db.Column(db.String(60))
    
    def __init__(self, data):
        self.id_task = data["id_task"]
        self.titulo = data["id_producto"]
        self.descripcion = data["version"]
        self.ftiempo_estimado_finalizacion = dt.datetime.strptime(data["tiempo_estimado_finalizacion"], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.horas_acumuladas = data["horas_acumuladas"]
        self.estado = data["estado"]
        self.responsable = data["responsable"]

    def update_data(self, data):
        self.id_task = data["id_task"]
        self.titulo = data["titulo"]
        self.descripcion  = data["descripcion "]
        self.tiempo_estimado_finalizacion = dt.datetime.strptime(data["tiempo_estimado_finalizacion"], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.horas_acumuladas = data["horas_acumuladas"]
        self.estado = data["estado"]
        self.responsable = data["responsable"]

    def to_dict(self):
        return {
            "id_task": self.id_task,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "tiempo_estimado_finalizacion ": self.tiempo_estimado_finalizacion.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "horas_acumuladas": self.horas_acumuladas,
            "estado": self.estado,
            "responsable": self.responsable,
        }
