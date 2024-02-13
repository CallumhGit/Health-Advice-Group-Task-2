# Importing the necessary modules that are used wtihin this file
from database import db 
from flask_login import UserMixin


class HealthCondition(db.Model, UserMixin):

    __tablename__ = "health-conditions"

    conid = db.Column(db.Integer, primary_key = True)

    uid = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable = True)

    conditionName = db.Column(db.String(50), nullable = False, unique= True)

    description = db.Column(db.String(50), nullable = False, unique = True)

    def get_id(self):
        return str(self.conid)
    
    def __repr__(self):
        return f"<Condition{self.conditionName}>"