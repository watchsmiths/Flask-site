from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, Form, TextAreaField
from validators import DataRequired

# class RegistrationForm(Form):
#     firstname = StringField('First Name', [validators.Length(min=4, max=25)])
#     lastname = StringField('Last Name', [validators.Length(min=4, max=25)])
#     email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
#     password = PasswordField('New Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = PasswordField('Repeat Password')

# class LoginForm(Form):
#     email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
#     password = PasswordField('New Password', [validators.DataRequired()])

# class newsletter(FlaskForm)


# class Contact(Form):
#     firstname = StringField('First Name', [validators.Length(min=4, max=25)])
#     email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
#     password = PasswordField('New Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = PasswordField('Repeat Password')


class Sellwatch(Form):
    firstname = StringField('First Name', [validators.Length(min=4, max=25)])
    lastname = StringField('Last Name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
 