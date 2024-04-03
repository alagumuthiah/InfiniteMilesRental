from flask import Flask, render_template
from flask_migrate import Migrate
from .config import Config
from .models import db
from .api.booking_routes import booking_routes
from .api.car_routes import car_routes
from .api.search_routes import search_routes
from .seeder import seed_commands

app = Flask(__name__)
app.config.from_object(Config)
app.cli.add_command(seed_commands)
app.register_blueprint(booking_routes, url_prefix='/api/bookings')
app.register_blueprint(car_routes,url_prefix='/api/cars')
app.register_blueprint(search_routes,url_prefix='/api/search')


db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Car Rental Application</h1>'
