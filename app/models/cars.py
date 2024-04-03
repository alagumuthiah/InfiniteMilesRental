from .db import db

class Car(db.Model):
    __tablename__ ='cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    categoryId = db.Column(db.Integer, db.ForeignKey('categories.id'))
    supplierId = db.Column(db.Integer, db.ForeignKey('suppliers.id'))
    gear = db.Column(db.Enum('Manual','Automatic',name='gear_enum'), nullable=False)
    images = db.Column(db.String(255))
    locationId = db.Column(db.Integer, db.ForeignKey('location.id'))

    supplier = db.relationship('Supplier', back_populates='cars')
    category = db.relationship('Category',back_populates='cars')
    location = db.relationship('Location',back_populates='cars')
    bookings = db.relationship('Booking',back_populates='car')

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

#  * Id
#     * Name
#     * SupplierId (Foreign Key)
#     * Category Id (Foreign Key) - Can be an array that accepts multiple values
#     * Gear (Automatic/Manual)
#     * Images
#     * locationId (Foreign Key) - Base location
