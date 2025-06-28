from datetime import datetime, timezone, date

from . import db

class BaseModel(db.Model):
    __abstract__ = True

    def to_dict(self):
        result = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if isinstance(value, (datetime, date)):
                result[column.name] = value.isoformat()
            else:
                result[column.name] = value
        return result

class Patient(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    # need to initiatate
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)

    # auto generated on init
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=datetime.now(timezone.utc), nullable=True)
    active = db.Column(db.Boolean(), default=True)

    # not necessary for sqlalchemy but helpful for code completion during development
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def __repr__(self):
        return f"<Patient {self.first_name} {self.last_name}>"
    
    