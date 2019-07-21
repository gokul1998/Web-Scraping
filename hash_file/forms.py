from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):

    name = StringField('Name',validators=[DataRequired(),Length(min=6, max=20),])
    username = StringField('Username',validators=[DataRequired(),Length(min=6 ,max=50)])
    email= StringField ('Email',validators=[DataRequired(),Email()])
    password= PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):

    username=StringField('Username',validators=[DataRequired(),Length(min=6 ,max=50)])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember me')
    submit=SubmitField('Sign In')
