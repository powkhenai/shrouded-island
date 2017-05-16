import hashlib
from app import app, db, lm
from flask import Flask, render_template, session, redirect, url_for, request, flash, g
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, NewCharForm
from .models import User, Character

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
        #flash('Token="%s", remember_me=%s' % 
        #(form.login_token.data, str(form.remember_me.data)))
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
    characters = Character.query.filter_by(user_id=user.id).all()
    print characters
    return render_template('test.html', name=user.name, characters=characters)

@app.route('/character/<char_id>')
@login_required
def show_char(char_id):
    user = g.user
    character = Character.query.get(char_id)
    print character
    if character.player != user:
        return redirect(url_for('index'))
    return render_template('char_sheet.html', user=user, character=character)

@app.route('/new_character', methods=['GET', 'POST'])
@login_required
def newChar():
    user = g.user
    form = NewCharForm()
    if form.validate_on_submit():
        character = Character(first_name=form.first_name.data, last_name=form.last_name.data,
                              height=form.height.data, weight=form.weight.data,
                              age=form.age.data, hp=form.hp.data,
                              exp=form.exp.data, iq=form.iq.data,
                              me=form.me.data, ma=form.ma.data,
                              ps=form.ps.data, pp=form.pp.data,
                              pe=form.pe.data, pb=form.pb.data,
                              spd=form.spd.data, player=user)
        db.session.add(character)
        db.session.commit()
        flash('User: %s ID: %d' % (user.name, user.id))
        flash('%s %s %d' % (form.first_name.data, form.last_name.data, form.age.data))
        return redirect(url_for('index'))
    return render_template('newchar.html', title='New Character', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
