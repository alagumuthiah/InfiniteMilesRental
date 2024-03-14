from .db import db
# - Reviews
#     * ReviewId
#     * UserID (Foreign Key)
#     * CategoryId (Foreign Key)
#     * SupplierId (Foreign Key)
#     * Star Review (out of 10)
#     * Value for Money (out of 10)
#     * Car cleanliness (out of 10)
#     * Car condition (out of 10)
#     * Pick up speed (out of 10)


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,db.ForeignKey('users.id'))
    categoryId = db.Column(db.Integer,db.ForeignKey('categories.id'))
    supplierId = db.Column(db.Integer,db.ForeignKey('suppliers.id'))
    starReview = db.Column(db.Enum(*map(str, range(1, 11)),name='starReview_enum'))
    valueForMoney = db.Column(db.Enum(*map(str, range(1, 11)),name='valueForMoney_enum'))
    cleanliness = db.Column(db.Enum(*map(str, range(1, 11)),name='cleanliness_enum'))
    condition = db.Column(db.Enum(*map(str, range(1, 11)),name='condition_enum'))
    pickUpSpeed = db.Column(db.Enum(*map(str, range(1, 11)),name='pickUpSpeed_enum'))

    user = db.relationship('User',back_populates='reviews')
    category = db.relationship('Category',back_populates='reviews')
    supplier = db.relationship('Supplier',back_populates='reviews')
