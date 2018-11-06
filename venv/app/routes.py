from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect

# These are called 'view' functions.  (Think MVT, not MVC)
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Quincy'}
    posts = [
        {
            'author': {'username' : 'Quincy'},
            'body': 'Beautiful day in Louisville!'
        },
        {
            'author': {'username': 'Lily'},
            'body': 'I love Sun Chips!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # passing the form object into the template with the name form
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)