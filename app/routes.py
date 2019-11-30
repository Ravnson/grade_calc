from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.grades.db import db_manager

@app.route('/')
@app.route('/index')
def index():
    course = {'name': 'KS1'}
    return render_template('index.html', title='Home', course=course)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/classes')
def classes():   
    classes = db_manager.get_classes()
    return render_template('classes.html', title='Classes', classes=classes)

@app.route('/class/<cla>')
def cla(cla):
    return render_template('class.html')