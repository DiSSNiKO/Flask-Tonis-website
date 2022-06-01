from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError


class RegisterForm(FlaskForm):
    username = StringField(label='username', validators=[Length(min=2,max=30), DataRequired()])
    email = StringField(label='email', validators=[Length(min=10,max=50), DataRequired()])
    password1 = PasswordField(label='password',validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='repeat password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='username', validators=[Length(min=2,max=30), DataRequired()])
    password = PasswordField(label='password',validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label='Login')
    
class postForm(FlaskForm):
    content = StringField(label='post', validators=[Length(min=2,max=200), DataRequired()])
    submit = SubmitField(label='POST')
    