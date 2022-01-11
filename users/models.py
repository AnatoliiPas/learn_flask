from datetime import datetime
from enum import unique

from db import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128))
    color = db.Column(db.String(120))
    created_add = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'{self.name}'


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    autor = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow())
