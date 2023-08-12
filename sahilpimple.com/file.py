# from  flask_wtf import Flaskform 
# from wtforms import StringField , PasswordField , SubmitField , BooleanField
# from wtforms.validators import Datarequired , length , Email , EqualTo
# class Registrationfrom(Flaskform):
#  username = StringField('Usernsame',
#                         validators=[Datarequired(),length(min=2,max=20) ])
# Email = StringField('Email',
#                         validators=[Datarequired(),Email() ])
# password = PasswordField ('password',validators=[Datarequired()])
# confirm_password = PasswordField('confirm password',
#                          validators=[Datarequired() , EqualTo('password')])

# submit = SubmitField('Sign Up')
# from  flask_wtf import Flaskform 
# from wtforms import StringField , PasswordField , SubmitField
# from wtforms.validators import Datarequired , length , Email , EqualTo

# class Loginform(Flaskform):
#  Email = StringField('Email',
#                         validators=[Datarequired(),Email() ])
# password = PasswordField ('password',validators=[Datarequired()])
# remember = BooleanField('Remember Me')

# submit = SubmitField('Log In')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
