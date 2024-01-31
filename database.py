# Import the SQLAlchemy class from the Flask-SQLAlchemy extension
from flask_sqlalchemy import SQLAlchemy

# Define the SQLite database URI
sqlite = "sqlite:///database.db"

# Create an instance of the SQLAlchemy class
db = SQLAlchemy