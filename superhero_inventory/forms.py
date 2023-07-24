from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('E-mail', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()


class SuperheroForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    price = DecimalField('price')
    appeared = StringField('comics appeared in')
    superpowers = StringField('Superpowers')
    submit_button = SubmitField()