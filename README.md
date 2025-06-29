# Patient Portal

## To run
1. create a virtual environment such as `python3 -m venv venv`
2. activate virtual environment such as `source venv/bin/activate`
3. install dependencies with `pip install -r requirements.txt`
4. run application with `python3 run.py`

## Additional Questions
1. Form validation is handled by Flask-WTF, which integrates WTForms for validation and rendering
for front end and back end validation. Custom validators, such as the date of birth validator, are
written in Python. Messages of errors, labels, and submit button are also written in Python. It is my
opinion that this makes consistency and internationalization simpler to maintain.

2. I would implement auth with Flask-Security. Flask-Security includes Flask-Login but includes 
more secure features including emailing users when their login credentials are changed, emailing
instructions to reset their password if it has been forgotten or compromised,  allowing role 
permissions so that admins can have control such as creating users, disabling logins, 
resetting passwords, and other features that would be useful for HIPAA compliance.

3. Any cloud provider under consideration would need to be thoroughly assessed for their 
ability to be HIPAA compliant. Additonally, the cloud provider would need to sign a 
Business Associate Agreement and development may be limited to the cloud services agreed 
upon. When I worked for Mobius Medical Systems, we reduced our risk by storing PHI on site
of our customers instead of in the cloud. Each of our customers hosted their own databases.

4. This sample project does not support database migrations. I would add Flask-Migrate to
easily perform SQL migrations with Alembic.Services including mail, security, and database
initialization are activated in create_app in app/__init__.py, but for organization I like
to have a services.py that includes the configuration and is then imported and connected to 
the application by create_app.  

