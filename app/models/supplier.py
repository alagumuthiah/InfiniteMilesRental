from .db import db

class Supplier(db.Model):
    __tablename__='suppliers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
