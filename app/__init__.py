from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config


"""Construct the core app object."""
app = Flask(__name__, instance_relative_config=False)

db = SQLAlchemy(app)

# Application Configuration
app.config.from_object(Config)

# db.init_app(app)

with app.app_context():
    from app import routes
    from app.Users.models import *

    # Create Database Models
    db.create_all()
