from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class GoForm(FlaskForm):
    left = StringField('left', validators=[DataRequired()])
    right = StringField('right', validators=[DataRequired()])
    submit = SubmitField('GO!')

class GoFormInt(FlaskForm):
    left = IntegerField('left', validators=[NumberRange(-100,100,
        "max duty cycle 100%")])
    right = IntegerField('right', validators=[NumberRange(-100,100,
        "max duty cycle 100%")])
    submit = SubmitField('GO!')

