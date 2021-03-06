import logging
from logging.handlers import SMTPHandler
from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel

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

# Flask Bootstrap support
bootstrap = Bootstrap(app)

# Flask Mail support
# TODO complete config w/ gmail address
mail = Mail(app)

# Support for precise time via Flask-Moment / Moment.js
moment = Moment(app)

# Language support
babel = Babel(app)
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# This is referencing the package and __init__.py script seen here.
# The import is located here to avoid "circular imports" common to Flask.

# Setting up error logging to email when in production

"""Creates an SMTPHandler instance, sets level to report only errors, no warnings,
info, or debug msgs, and attaches it to the app.logger object from Flask"""
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler =SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no_reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject="Cheesecake Blog Failure",
                credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

# Models defines the db structure
from app import routes, models, errors