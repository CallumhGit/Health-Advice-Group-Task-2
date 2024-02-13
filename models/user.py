# Importing the necessary modules that are used wtihin this file
from database import db 
from flask_login import UserMixin

# creates a class that represents the User Model and inherits from db.Model and UserMixing
class User(db.Model, UserMixin):

    # Set the table name for the model
    __tablename__ = "users"

    # Define the columns that can be found within the table
    uid = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(20), nullable = False, unique= True)

    password = db.Column(db.String(500), nullable = False)

    avatar = db.Column(db.String(200), nullable= False, default = "default.png")

    usergroup = db.Column(db.SmallInteger, nullable = False, default = 0)

    conditions = db.relationship('HealthCondition', backref='user', lazy=True)

    # Defines a method to get the user ID
    def get_id(self):
        return self.uid
    
    # Defines  a string representation of the user object
    def __repr__(self):
        return f"<User{self.username}>"