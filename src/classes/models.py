from __main__ import app
from email.policy import default
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
    family = db.relationship('familyClass', backref='socio', lazy=True)
    withDebt = db.Column(db.Boolean, nullable = False)
    debts = db.relationship('debtClass', backref='socio', lazy=True)
    typeSocio= db.Column(db.String(80), nullable = False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, lastname, age, address, dni, phone, email, wayToPay, permission, family, withDebt, debt, typeSocio):
        super().__init__(name, lastname, age, address, dni, phone, email)
        self.wayToPay = wayToPay
        self.permission = permission
        self.family = family
        self.withDebt = withDebt
        self.debt = debt
        self.typeSocio = typeSocio

class familyClass(personClass, db.Model):
    __tablename__ = 'family'
    id = db.Column(db.Integer, primary_key=True)
    familyId = db.Column(db.Integer, db.foreign_key('socio.id'), nullable=False)
    relationship = db.Column(db.String(80), nullable=False)
    permissions = db.Column(db.String(80), nullable=False)
    typeSocio= db.Column(db.String(80), nullable = False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, lastname, age, address, dni, phone, email, familyId, relationship, permissions, typeSocio):
        super().__init__(name, lastname, age, address, dni, phone, email)
        self.familyId = familyId
        self.relationship = relationship
        self.permissions = permissions
        self.typeSocio = typeSocio


class debtsClass(db.Model):
    __tablename__ = 'debts'
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Integer, nullable=False)
    debtorId = db.Column(db.Integer, db.foreign_key('socio.id'), nullable=False)
    reazon = db.Column(db.String(80), nullable=False)
    dateOfDebt = db.Column(db.DateTime, nullable=False)
    state = db.Column(db.String(80), nullable=False)
    pays = db.relationship('payClass', backref='debts', lazy=True)
    dueDebt = db.Column(db.DateTime, nullable = False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, amount, debtorId, reazon, dateOfDebt, state, dueDebt):
        self.amount = amount
        self.debtorId = debtorId
        self.reazon = reazon
        self.dateOfDebt = dateOfDebt
        self.state = state
        self.dueDebt = dueDebt

class payClass(db.Model):
    __tablename__ = 'pay'
    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Integer, nullable=False)
    payerId = db.Column(db.Integer, db.foreign_key('socio.id'), nullable=False)
    dateOfPay = db.Column(db.DateTime, nullable=False)
    debtId = db.Column(db.Integer, db.foreign_key('debts.id'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, amount, payerId, dateOfPay, debtId):
        self.amount = amount
        self.payerId = payerId
        self.dateOfPay = dateOfPay
        self.debtId = debtId

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
