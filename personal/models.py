from datetime import datetime

from pms import db


class Department(db.Model):
    """部门"""
    __tablename__ = 'department'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<部门 {self.id}: {self.name}>'


class Employee(db.Model):
    """员工"""
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gender = db.Column(db.String)
    job = db.Column(db.String)
    birthdate = db.Column(db.DateTime)
    idcard = db.Column(db.String)
    address = db.Column(db.String)
    salary = db.Column(db.Float)
    release_time = db.Column(db.DateTime)

    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department', backref=db.backref('employees', lazy='dynamic'))

    def __init__(self, name, gender, job, birthdate, idcard, address, salary, release_time=None):
        self.name = name
        self.gender = gender
        self.job = job
        self.birthdate = birthdate
        self.idcard = idcard
        self.address = address
        self.salary = salary
        self.release_time = release_time if release_time else datetime.now()

    def __repr__(self):
        return f'<员工 {self.id}: {self.name} {self.salary} {self.address} >'
