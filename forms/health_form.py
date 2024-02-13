from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

# Form for adding health conditions
class HealthConditionForm(FlaskForm):
    conditionName = StringField(validators=[InputRequired(), Length(min=3, max=50)], render_kw={"placeholder": "Enter the condition name..."})
    description = StringField(validators=[InputRequired(), Length(min=3, max=50)], render_kw={"placeholder": "Enter a description..."})
    submit = SubmitField("Add Condition")