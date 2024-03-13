from .db import db

class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255))
    lastName = db.Column(db.String(255))
    email = db.Column(db.String(255))
    hashedPassword = db.Column(db.String(255))
    loginMethod = db.Column(db.Enum('traditional', 'google','github', name='login_method_enum'), nullable=False)