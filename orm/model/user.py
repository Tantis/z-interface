
from interface import db

__all__ = ['User']


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __init__(self, id, name):
        self.id = id
        self.name = name
