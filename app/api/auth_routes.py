from flask import Blueprint, jsonify, request, redirect, url_for
from flask_login import login_user
from app.models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

auth_routes = Blueprint('auth',__name__)


@auth_routes.route('/signup', methods=['POST'])
def signup():
    userDetails = request.json
    firstName = userDetails.get('firstName')
    lastName = userDetails.get('lastName')
    email = userDetails.get('email')
    password = userDetails.get('password')

    # Check if username already exists
    if User.query.filter_by(email=email).first():
        return 'User with the given email already exists, try again with a different email', 400

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

    return jsonify(new_user.to_dict()), 200

@auth_routes.route('/login', methods=['POST'])
def login():
    print('inside login')
    print(request.json)
    credentials  = request.json
    email = credentials.get('email')
    password = credentials.get('password')

    # Retrieve user from database
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.hashedPassword, password):
        login_user(user)
        return jsonify(user.to_dict()), 200
    else:
        return 'Incorrect username or password', 401
