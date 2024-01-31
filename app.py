#Importing of the modules that are going to be used within in this file
from flask import Flask, render_template, redirect, url_for
from database import db, sqlite
from extension import argon2 
from forms.user_forms import RegisterForm, LoginForm
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from models.user import User
from sqlalchemy import text

# Import the Flask module and create an instance of the Flask application
app = Flask(__name__)

# Initialize the Argon2 password hashing library with the Flask application
argon2.init_app(app)


# Configure the SQLite database URI for the application
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite

# Set the secret key for the application
app.config["SECRET_KEY"] = "healthAdvice1234"

# Initialize the SQLAlchemy database with the Flask application
db.init_app(app)


# Create the database tables using the SQLAlchemy models
with app.app_context():
    db.create_all()

# Create an instance of the LoginManager for handling user authentication
login_manager = LoginManager()
login_manager.init_app(app)

# Set the login view for the application
login_manager.login_view = "Login"


# Define a user loader function for the LoginManager to load users from the database
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define a route for the root URL ("/") that renders the index.html template
@app.route("/")
def index():
    return render_template("index.html")