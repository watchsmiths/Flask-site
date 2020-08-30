from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, BooleanField, FileField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Required
from wtforms.fields.html5 import EmailField
from wtforms import validators


class Sellwatch(FlaskForm):
    yourname = StringField('Your Name', [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Length(min=6, max=35), validators.Email("This field requires a valid email address")])
    brand = StringField('Brand Name', [validators.DataRequired(), validators.Length(min=4, max=25)])
    model = StringField('Model/Model Number', [validators.DataRequired(), validators.Length(min=4, max=25)])
    age = IntegerField('Age (Years)', [validators.Length(min=4, max=25)])
    box = SelectField('Box', choices={('Yes','Yes'), ('No','No')}, default='Yes')
    papers = SelectField('Papers', choices={('Yes','Yes'), ('No','No')}, default='Yes')
    description = TextAreaField('Brief Description of item', [validators.optional(), validators.Length(min= 14, max=500)])
    image = FileField('Photo (Required)', [validators.DataRequired()])
    submit = SubmitField('Submit')

class Contact(FlaskForm):
    yourname = StringField('Your Name', [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = EmailField('Email Address', [validators.DataRequired(), validators.Length(min=6, max=35), validators.Email("This field requires a valid email address")])
    description = TextAreaField('Brief Description of item', [validators.optional(), validators.Length(min= 14, max=500)])
    submit = SubmitField('Submit')

class newsletter(FlaskForm):
    email = EmailField('Email Address', [validators.DataRequired(), validators.Length(min=6, max=35), validators.Email("This field requires a valid email address")])
    


# class RegistrationForm(FlaskForm):
#     firstname = StringField('First Name', validators=[Length(min=4, max=25)])
#     lastname = StringField('Last Name', validators=[Length(min=4, max=25)])
#     email = StringField('Email Address', validators=[Length(min=6, max=35), Email()])
#     password = PasswordField('New Password', validators=[required(), EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = PasswordField('Repeat Password')

# class LoginForm(FlaskForm):
#     email = StringField('Email Address', validators=[Length(min=6, max=35), Email()])
#     password = PasswordField('New Password', validators=[DataRequired()])




