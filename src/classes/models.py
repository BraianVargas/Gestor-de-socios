import imp

from __main__ import app
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy(app)

class personClass(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(80), nullable=False)
    dni = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, lastname, age, address, dni, phone, email):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.address = address
        self.dni = dni
        self.phone = phone
        self.email = email


class socioClass(personClass, db.Model):
    __tablename__ = 'socio'
    id = db.Column(db.Integer, primary_key=True)
    wayToPay = db.Column(db.String(80), nullable=False)
    permission = db.Column(db.String(80), nullable = False)
    familyGroup = db.Column(db.String(80), nullable = False) #Esto deberia ser una lista con todos los familiares del socio
    debt = db.Column(db.Boolean, default=False)
    debtAmount = db.Column(db.Integer, nullable=False)
    debtDate = db.Column(db.DateTime, nullable=False)

class debtsClass(db.Model):
    __tablename__ = 'debts'
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(80), nullable=False)
    socio_id = db.Column(db.Integer, db.ForeignKey('socio.id'), nullable=False)
    




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    socio_id = db.Column(db.Integer, db.ForeignKey('socio.id'), nullable=False)
    

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    is_locked = db.Column(db.Boolean, default=False)
    is_logged_in = db.Column(db.Boolean, default=False)
    is_online = db.Column(db.Boolean, default=False)
    is_blocked = db.Column(db.Boolean, default=False)
    is_verified = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False) 
    is_user = db.Column(db.Boolean, default=False)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
