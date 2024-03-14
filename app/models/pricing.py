from .db import db

class Pricing(db.Model):
    __tablename__ = 'pricing'

    id = db.Column(db.Integer, primary_key=True)
    categoryId = db.Column(db.Integer, db.ForeignKey('categories.id'))
    supplierId = db.Column(db.Integer, db.ForeignKey('suppliers.id'))
    locationId = db.Column(db.Integer, db.ForeignKey('location.id'))
    price = db.Column(db.Numeric(scale=2)) #each day
    protectionCost = db.Column(db.Numeric(scale=2)) #for each day

    supplier = db.relationship('Supplier', back_populates='pricings')
    category = db.relationship('Category',back_populates='pricings')
    location = db.relationship('Location',back_populates='pricings')

#    * id
#     * categoryId (Foreign Key)
#     * supplier Id (Foreign Key)
#     * date
#     * price
