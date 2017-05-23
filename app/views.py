import hashlib
from app import app, db, lm
from flask import Flask, render_template, session, redirect, url_for, request, flash, g
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm
from .models import User

@app.before_request
def before_request():
    #session.clear()
    g.user = current_user

@app.route('/')
def hello_world():
    if g.user:
       return "Logged in as: %s" % g.user
    return "Not logged in."

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        flash('Token="%s", remember_me=%s' % 
                (form.login_token.data, str(form.remember_me.data)))
        user = User.query.filter_by(name=form.name.data).first()
        if user.login_token == unicode(hashlib.sha256(form.login_token.data).hexdigest()):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        else:
            flash('Invalid login information')
    return render_template('signin.html', title='Sign In', form=form)

@app.route('/characters')
@login_required
def index():
    user = g.user
    return render_template('test.html', username=user.name)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
