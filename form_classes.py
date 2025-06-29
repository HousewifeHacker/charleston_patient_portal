from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField, ValidationError
from wtforms.validators import InputRequired
from datetime import date

class PatientForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    dob = DateField('Date of Birth', validators=[InputRequired()])
    physician = StringField('Therapist', validators=[InputRequired()])
    submit = SubmitField('Add Patient')

    # custom validator
    def validate_dob(self, field):
        if field.data and field.data >= date.today():
            raise ValidationError("Date of birth must be in the past.")