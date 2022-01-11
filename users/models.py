from datetime import datetime

from db import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128))
    color = db.Column(db.String(120))
    created_add = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'{self.name}'
