""" How To Use and Validate Web Forms with Flask-WTF
https://www.digitalocean.com/community/tutorials/how-to-use-and-validate-web-forms-with-flask-wtf """

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, Length, InputRequired

class RegForm(FlaskForm):
    email = StringField('Email',  validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=20)])
    name = StringField('Name')
