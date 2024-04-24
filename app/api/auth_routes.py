from flask import Blueprint, jsonify, request, redirect, url_for
from flask_login import login_user
from app.models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

auth_routes = Blueprint('auth',__name__)


@auth_routes.route('/signup', methods=['POST'])
def signup():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    email = request.form['email']
    password = request.form['password']

    # Check if username already exists
    if User.query.filter_by(email=email).first():
        return 'Username already exists', 400

    # Hash the password
    hashedPassword = generate_password_hash(password)

    # Create new user
    new_user = User(firstName=firstName,
                    lastName=lastName,
                    email=email,
                    hashedPassword=hashedPassword,
                    loginMethod='traditional')
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth_routes.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Retrieve user from database
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.hashedPassword, password):
        login_user(user)
        return 'Logged in successfully'
    else:
        return 'Incorrect username or password', 401
