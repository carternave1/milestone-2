from app import app
from app.ReviewForm import ReviewForm
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for, request, Flask


@app.route('/')
@app.route('/index.html')
def index():
    user = {'username': 'Miguel'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route("/")
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route("/")
@app.route('/Mcdonalds.html', methods=['GET', 'POST'])
def Mcdonalds():
    form = ReviewForm()
    if form.validate_on_submit():
        flash('review sent from user "{}"'.format(form.text.data))
        return redirect(url_for('Mcdonalds'))
    return render_template('Mcdonalds.html', title="Review", form=form)


@app.route("/")
@app.route('/palms.html', methods=['GET', 'POST'])
def palms():
    form = ReviewForm()
    if form.validate_on_submit():
        flash('review sent from user "{}"'.format(form.text.data))
        return redirect(url_for('palms'))
    return render_template('palms.html', title="Review", form=form)

@app.route("/")
@app.route('/ott.html', methods=['GET', 'POST'])
def ott():
    form = ReviewForm()
    if form.validate_on_submit():
        flash('review sent from user "{}"'.format(form.text.data))
        return redirect(url_for('ott'))
    return render_template('ott.html', title="Review", form=form)

@app.route("/")
@app.route('/stavros.html', methods=['GET', 'POST'])
def stavros():
    form = ReviewForm()
    if form.validate_on_submit():
        flash('review sent from user "{}"'.format(form.text.data))
        return redirect(url_for('stavros'))
    return render_template('stavros.html', title="Review", form=form)

@app.route("/")
@app.route('/chubbys.html', methods=['GET', 'POST'])
def chubbys():
    form = ReviewForm()
    if form.validate_on_submit():
        flash('review sent from user "{}"'.format(form.text.data))
        return redirect(url_for('chubbys'))
    return render_template('chubbys.html', title="Review", form=form)