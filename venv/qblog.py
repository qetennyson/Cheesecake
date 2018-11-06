from app import app

# This top level script defines the Flask application instance.
# We are importing the app variable, containing the Flask instance, from the app package.

# This import also preps our Flask shell so that we can easily experiment in the
# Python interpreter without repeatedly invoking the imports.
from app import db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


