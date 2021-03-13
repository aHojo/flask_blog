from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andrew'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    """
    When the browser sends the POST request as a result of the user pressing the submit button, form.validate_on_submit() is going to gather all the data, run all the validators attached to fields, and if everything is all right it will return True, indicating that the data is valid and can be processed by the application. 
    """
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
