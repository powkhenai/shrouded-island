from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    login_token = PasswordField('login_token', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class NewCharForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('first_name', validators=[DataRequired()])
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
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    category = SelectField('Skill Category', choices=[('Communication', 'Communication'), ('Cowboy', 'Cowboy'),
        ('Domestic', 'Domestic'), ('Electrical', 'Electrical'), ('Espionage', 'Espionage'), ('Horsemanship', 'Horsemanship')])
    base = IntegerField('base', validators=[DataRequired()])
    per_level = IntegerField('Per Level', validators=[DataRequired()])
