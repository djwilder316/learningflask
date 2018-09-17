from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators



class SignupForm(Form):
    first_name = StringField('First name', [validators.DataRequired("Please enter your first name.")])
    last_name = StringField('Last name', [validators.DataRequired(message="Please enter your last name.")])
    email = StringField('Email', [validators.Email(message="Please enter your email.")])
    password = PasswordField('Password', [validators.DataRequired(message="Please enter a password."), validators.Length(min=6, message="Password must be more than 5 characters long.")])
    submit = SubmitField('Sign up')

class LoginForm(Form):
    email = StringField('Email', [validators.Email(message="Please enter your eamil address.")])
    password = PasswordField('Password', [validators.DataRequired(message="Please enter a password.")])  
    submit = SubmitField('Sign in')

class AddressForm(Form):
    address = StringField('Address', [validators.DataRequired("Please enter an address.")])
    submit = SubmitField("Search")
