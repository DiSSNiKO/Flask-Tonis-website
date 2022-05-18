from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email = StringField(label='email')
    password1 = StringField(label='password')
    password2 = StringField(label='repeat password')
    submit = SubmitField(label='submit')
