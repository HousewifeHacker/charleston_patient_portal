from flask import request, jsonify, render_template, redirect, url_for, flash
from datetime import datetime 

from . import db
from .models import Patient
from flask import current_app as app
from .form_classes import PatientForm

@app.route('/')
def home():
    """ Table of all patient data in the database """
    patients = Patient.query.all()
    return render_template("patients_table.html", patients=patients)

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    """ PatientForm for UI, handled getting, posting, and validating form with flask_wtf"""
    form = PatientForm()
    # POST
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        physician = form.physician.data
            
        item = Patient(
            first_name=first_name, 
            last_name=last_name, 
            dob=dob, 
            physician=physician
        )
        db.session.add(item)
        db.session.commit()
        flash('New patient added.', 'success')
        return redirect(url_for('home'))
    # form was submitted, validation failed
    elif form.is_submitted():
        flash('Please correct the errors in the form.', 'error')

    # GET, also if form validation fails
    return render_template('add_patient.html', form=form)
