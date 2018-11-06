from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# The actual instance of Flask and a member of the app package.
app = Flask(__name__)

# Pulls in our app configuration
app.config.from_object(Config)

# This represents our actual db object.
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login object
login = LoginManager(app)
login.login_view = 'login'

# This is referencing the package and __init__.py script seen here.
# The import is located here to avoid "circular imports" common to Flask.

# Models defines the db structure
from app import routes, models