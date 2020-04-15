from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for, request, Flask
from wtforms.validators import DataRequired


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route("/")
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/Mcdonalds', methods=['POST'])
def Mcdonalds():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text, render_template('Mcdonalds.html'), redirect(url_for('index'))

@app.route('/palms', methods=['POST'])
def palms():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text, render_template('palms.html'), redirect(url_for('index'))

@app.route('/otts', methods=['POST'])
def otts():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text, render_template('ott.html'), redirect(url_for('index'))

@app.route('/stavros', methods=['POST'])
def stavros():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text, render_template('stavros.html'), redirect(url_for('index'))

@app.route('/chubbys', methods=['POST'])
def chubbys():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text, render_template('chubbys.html'), redirect(url_for('index'))