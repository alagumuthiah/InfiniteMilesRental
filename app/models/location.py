from .db import db

class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    latitude = db.Column(db.Numeric(scale=6))
    longitude = db.Column(db.Numeric(scale=6))

    cars = db.relationship('Car',back_populates='location')
    pricings = db.relationship('Pricing', back_populates='location')
# - Location
#     * Id
#     * Name
#     * Latitude
#     * Longitude
