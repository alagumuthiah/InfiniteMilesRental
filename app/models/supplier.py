from .db import db

class Supplier(db.Model):
    __tablename__='suppliers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)

    pricings = db.relationship('Pricing', back_populates='supplier')
    cars = db.relationship('Car',back_populates='supplier')
    reviews = db.relationship('Review',back_populates='supplier')
