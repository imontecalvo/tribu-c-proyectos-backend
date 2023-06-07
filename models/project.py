from utils.db import db
import datetime as dt

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    cost = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(), default=dt.datetime.now())

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "cost":self.cost,
            "created_at":self.created_at
        }
