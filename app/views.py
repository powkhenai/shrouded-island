import hashlib
from app import app, db, lm
from flask import Flask, render_template, session, redirect, url_for, request, flash, g, jsonify
from flask.json import dumps
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, NewCharForm, NewSkillForm, AddSkillToChar, ChangePasswordForm
from .models import User, Character, Skill, SkillCategory, CharSkills, Alignment

@app.before_request
def before_request():
    #session.clear()
    g.user = current_user

@app.route('/')
def hello_world():
    return redirect(url_for('index'))

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
    return render_template('test.html', user=user, characters=characters)

@app.route('/character/<char_id>')
@login_required
def show_char(char_id):
    user = g.user
    character = Character.query.get(char_id)
    print character
    if character.player != user:
        return redirect(url_for('index'))
    return render_template('char_sheet.html', user=user, character=character)

@app.route('/character/<char_id>/skills', methods=['GET', 'POST'])
@login_required
def skill_page(char_id):
    user = g.user
    character = Character.query.get(char_id)
    form = AddSkillToChar()
    form.category.choices = [(0, 'Category')]
    form.category.choices.extend([(c.id, c.name) for c in SkillCategory.query.order_by('name')])
    form.skills.choices = []
    if request.method == 'POST':
        form.skills.choices = [(s.id, s.name) for s in Skill.query.filter_by(skill_category=form.category.data)]
    if character.player != user:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        for skill_id in form.skills.data:
            new_skill = CharSkills(skill_type=form.skill_type.data, class_bonus=form.bonus.data)
            new_skill.skill=Skill.query.get(skill_id)
            new_skill.character=character
        db.session.commit()
        return redirect(url_for('skill_page', char_id=char_id))
    else:
        for i in form.errors:
            print i
    return render_template('skills.html', user=user, character=character, form=form)


@app.route('/delete_character/<char_id>')
@login_required
def rmChar(char_id):
    user = g.user
    character = Character.query.get(char_id)
    if character.player != user:
        return redirect(url_for('index'))
    for skill in character.skills:
        db.session.delete(skill)
    db.session.delete(character)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/new_character', methods=['GET', 'POST'])
@login_required
def newChar():
    user = g.user
    form = NewCharForm()
    form.alignment.choices = [(c.id, c.name) for c in Alignment.query.order_by('name')]
    if form.validate_on_submit():
        character = Character(first_name=form.first_name.data, last_name=form.last_name.data,
                              height=form.height.data, weight=form.weight.data,
                              age=form.age.data, hp=form.hp.data,
                              exp=form.exp.data, iq=form.iq.data,
                              me=form.me.data, ma=form.ma.data,
                              ps=form.ps.data, pp=form.pp.data,
                              pe=form.pe.data, pb=form.pb.data,
                              spd=form.spd.data, player=user,
                              align=Alignment.query.get(form.alignment.data))
        db.session.add(character)
        db.session.commit()
        flash('User: %s ID: %d' % (user.name, user.id))
        flash('%s %s %d' % (form.first_name.data, form.last_name.data, form.age.data))
        return redirect(url_for('index'))
    return render_template('newchar.html', title='New Character', form=form)

@app.route('/newskill', methods=['GET', 'POST'])
@login_required
def newSkill():
    user = g.user
    form = NewSkillForm()
    form.category.choices = [(s.id, s.name) for s in SkillCategory.query.order_by('name')]
    if form.validate_on_submit():
        skill = Skill(name=form.name.data, description=form.description.data, skill_category=form.category.data,
                base=form.base.data, per_level=form.per_level.data, note=form.note.data)
        db.session.add(skill)
        db.session.commit()
        flash("Skill: %s added to the system" % (skill.name))
        return redirect(url_for('newSkill'))
    if request.method == 'POST':
        flash(form.errors)
        flash(form.category.choices)
        flash(form.category.data)
    return render_template('newskill.html', title='New Skill', user=user, form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<user_id>', methods=['GET', 'POST'])
@login_required
def user_profile(user_id):
    user = g.user
    form = ChangePasswordForm()
    success = False
    if user != User.query.get(int(user_id)):
        return redirect(url_for('index'))
    if form.validate_on_submit():
        auth = form.login_token.data
        user.login_token = hashlib.sha256(auth).hexdigest()
        db.session.commit()
        success=True
    return render_template('user_profile.html', title='User Profile', user=user, form=form, success=success)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/db/<category>/skills')
@login_required
def getSkillbyCategory(category):
    skill_array = (Skill.query.filter_by(skill_category=category).all())
    print dumps(skill_array)
    ret_data = jsonify('{"skills": %s}' % dumps(skill_array))
    return ret_data

@app.route('/db/character/<char_id>/skill/<skill_id>/remove')
@login_required
def remSkillFromChar(char_id, skill_id):
    user=g.user
    if user != Character.query.get(char_id).player:
        return redirect(url_for('index'))
    charskill = CharSkills.query.get((char_id, skill_id))
    db.session.delete(charskill)
    db.session.commit()
    return redirect(url_for('skill_page', char_id=char_id))
