from flask import Flask, render_template
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config
from .models import db, User
from .api.booking_routes import booking_routes
from .api.car_routes import car_routes
from .api.search_routes import search_routes
from .api.auth_routes import auth_routes
from .seeder import seed_commands

app = Flask(__name__)
app.config.from_object(Config)
app.cli.add_command(seed_commands)
app.register_blueprint(booking_routes, url_prefix='/api/bookings')
app.register_blueprint(car_routes,url_prefix='/api/cars')
app.register_blueprint(search_routes,url_prefix='/api/search')
app.register_blueprint(auth_routes,url_prefix='/api/auth')

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id): #By registering user_loader with login_manager - flask knows how to get the user details by using session cookies
    return User.query.get(int(user_id))

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Car Rental Application</h1>'
