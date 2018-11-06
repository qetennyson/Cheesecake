import os

# basic local SQlite DB
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # using a constant here to store this secret key value
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # talks to an external database or references the local SQLite DB file
    SQLALCHEMY_DATABASE_URI  = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # Can signal app each time a change is about to be made to the DB.  Not needed here.
    SQLALCHEMY_TRACK_MODIFICTIONS = False
