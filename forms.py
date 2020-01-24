from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class GoForm(FlaskForm):
    left = StringField('left', validators=[DataRequired()])
    right = StringField('right', validators=[DataRequired()])
    submit = SubmitField('GO!')

class Config(object):
    SECRET_KEY = 'my secret key'

