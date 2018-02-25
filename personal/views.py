from flask import render_template, redirect
from flask.views import MethodView
from pms import db
from .models import Employee, Department


class EmployeeListView(MethodView):
    def get(self):
        employees = db.session.query(Employee).all()[:10]
        return render_template('employee-list.html', employees=employees)

