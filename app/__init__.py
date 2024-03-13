from flask import Flask, render_template
from flask_migrate import Migrate
from .config import Config
from .models import db
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
@app.route('/')
def index():
    return '<h1>Car Rental Application</h1>'