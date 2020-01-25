from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

print('forms.py')

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

class Config(object):
    SECRET_KEY = 'my secret key'

