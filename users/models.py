from datetime import datetime
from flask_login import UserMixin

from conf import db


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128))
    about_author = db.Column(db.Text(), nullable=True)
    posts = db.relationship('Posts', backref='poster')
    created_add = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'{self.name}'
