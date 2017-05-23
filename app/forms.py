from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    login_token = PasswordField('login_token', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
