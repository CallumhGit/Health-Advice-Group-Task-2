#Importing the modules that will be used throughout this project
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
from models.user import User
from extension import argon2



# This form is used when users signup
class RegisterForm(FlaskForm):

    username = StringField(validators=[InputRequired(), Length( min = 3, max = 20, message= None)], render_kw={"placeholder": "Enter a username..."})

    password = PasswordField(validators=[InputRequired(), Length(min= 3), EqualTo("confirm", message= "Passwords do not match")], render_kw={"placeholder": "password"})

    confirm = PasswordField(render_kw={"placeholder": "confirm password"})

    submit = SubmitField("submit")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username = username.data).first()

        if existing_user_username:
            raise ValidationError("Username already exists")


# This is the form thats used for users to login
class LoginForm(FlaskForm):
    
    username = StringField(validators=[InputRequired()], render_kw={"placeholder": "username"})

    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "password"})

    remember = BooleanField("Remember Me")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username = username.data).first()

        if existing_user_username is None or not argon2.check_password_hash(existing_user_username.password, str(self.password.data)):
            raise ValidationError ("Username or password is incorrect, please try again")
    
        
    submit = SubmitField("submit")

























