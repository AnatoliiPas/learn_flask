from datetime import datetime
from db import db


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    autor = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.now())
