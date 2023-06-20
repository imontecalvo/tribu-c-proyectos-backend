from utils.db import db
import datetime as dt


class Project(db.Model):
    codigo = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer)
    id_producto = db.Column(db.Integer)
    version = db.Column(db.String(10))
    customizacion = db.Column(db.String(60))
    nombre = db.Column(db.String(60))
    fecha_inicio = db.Column(db.DateTime(), default=dt.datetime.now())
    fecha_fin_estimada = db.Column(db.DateTime())
    estado = db.Column(db.String(20), default="iniciado")
    horas_consumidas = db.Column(db.Integer, default=0)
    costo_estimado = db.Column(db.Integer)

    def __init__(self, data):
        self.id_cliente = data["id_cliente"]
        self.id_producto = data["id_producto"]
        self.version = data["version"]
        self.customizacion = data["customizacion"]
        self.nombre = data["nombre"]
        self.fecha_fin_estimada = dt.datetime.strptime(
            data["fecha_fin_estimada"], "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        self.costo_estimado = data["costo_estimado"]

    def update_data(self, data):
        self.id_cliente = data["id_cliente"]
        self.id_producto = data["id_producto"]
        self.version = data["version"]
        self.customizacion = data["customizacion"]
        self.nombre = data["nombre"]
        self.fecha_fin_estimada = dt.datetime.strptime(
            data["fecha_fin_estimada"], "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        self.estado = data["estado"]
        self.horas_consumidas = data["horas_consumidas"]
        self.costo_estimado = data["costo_estimado"]

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "id_cliente": self.id_cliente,
            "id_producto": self.id_producto,
            "version": self.version,
            "customizacion": self.customizacion,
            "nombre": self.nombre,
            "fecha_inicio": self.fecha_inicio.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "fecha_fin_estimada": self.fecha_fin_estimada.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"
            ),
            "estado": self.estado,
            "horas_consumidas": self.horas_consumidas,
            "costo_estimado": self.costo_estimado,
        }
