from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, IntegerField, SelectField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Optional, EqualTo

class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    login_token = PasswordField('login_token', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class NewCharForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('first_name', validators=[DataRequired()])
    alignment = SelectField('alignment', coerce=int)
    height = IntegerField('height')
    weight = IntegerField('weight')
    age = IntegerField('age')
    hp = IntegerField('hp')
    exp = IntegerField('exp')
    iq = IntegerField('iq')
    me = IntegerField('me')
    ma = IntegerField('ma')
    ps = IntegerField('ps')
    pp = IntegerField('pp')
    pe = IntegerField('pe')
    pb = IntegerField('pb')
    spd = IntegerField('spd')

class NewSkillForm(FlaskForm):
    category = SelectField('Skill Category', coerce=int)
    name = StringField('name', validators=[DataRequired()])
    base = IntegerField('base', validators=[DataRequired()])
    per_level = IntegerField('Per Level', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    note = TextAreaField('note', validators=[Optional(strip_whitespace=False)])

class AddSkillToChar(FlaskForm):
    category = SelectField('Skill Category', coerce=int)
    bonus = IntegerField('bonus', validators=[Optional()])
    skill_type = SelectField('Skill Type', choices=[('OCC', 'O.C.C. Skills'),('REL','O.C.C Related'), ('SEC', 'Secondary Skills')])
    skills = SelectMultipleField(u'Add Skills', coerce=int)

class ChangePasswordForm(FlaskForm):
    login_token = PasswordField('login_token', validators=[DataRequired(), EqualTo('match_token', message='Passwords must match')])
    match_token = PasswordField('match_token', validators=[DataRequired()])
