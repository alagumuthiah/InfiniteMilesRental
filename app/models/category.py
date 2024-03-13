from .db import db

# - Category (SUV, Sedan)
#     * id
#     * category (SUV, Car)
#     * subcategory(economy, compact, Mid-size, Standard, Full Size)
#     * Seats


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))
    subcategory = db.Column(db.String(255))
    seats = db.Column(db.Integer)
