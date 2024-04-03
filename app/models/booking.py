from .db import db

#   * bookingId
#     * email
#     * userId (foreign key from User table)
#     * pickup location
#     * pickup time
#     * drop location
#     * drop time
#     * carId - foreign key from car table (this gets updated when a user picks up a car)
#     * booking status (active/ inactive, completed) ( updated to active when the user picks up a car)
#     * protected - boolean
#     * cost (cost of the booking)

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    pickupLocation = db.Column(db.String(255))
    pickupTime = db.Column(db.DateTime())
    dropLocation = db.Column(db.String(255))
    dropTime = db.Column(db.DateTime())
    carId = db.Column(db.Integer, db.ForeignKey('cars.id'))
    categoryId = db.Column(db.Integer,db.ForeignKey('categories.id'))
    status = db.Column(db.Enum('Completed','Active','Inactive','Cancelled', name='booking_enum'))
    protected = db.Column(db.Boolean)
    cost = db.Column(db.Numeric(scale=2))
    paymentMethod = db.Column(db.Enum('Paypal','card','TBC',name='payment_enum'))

    user = db.relationship('User',back_populates='bookings')
    car = db.relationship('Car',back_populates='bookings')
    category = db.relationship('Category',back_populates='bookings')

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
