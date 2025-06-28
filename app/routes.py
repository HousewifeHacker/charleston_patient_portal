from flask import request, jsonify
from datetime import datetime 

from . import db
from .models import Patient
from flask import current_app as app

@app.route('/')
def home():
    items = Patient.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/add', methods=['POST'])
def add_patient():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    dob_str = data.get('dob')
    try:
        dob = datetime.strptime(dob_str, '%Y-%m-%d').date() if dob_str else None
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400
    if not first_name:
        return jsonify({'error': 'Name is required'}), 400
    item = Patient(first_name=first_name, last_name=last_name, dob=dob)
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': f'Patient "{first_name}" added successfully'})
