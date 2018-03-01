from flask import render_template, redirect, url_for, request
from flask.views import MethodView
from pms import db
from .models import Employee, Department
from personal.forms import EmployeeForm
from datetime import datetime


class EmployeeListView(MethodView):
    def get(self, page=1):
        items = Employee.query.paginate(page, per_page=10)
        return render_template('emp-list.html', employees=items)


class EmployeeDelView(MethodView):
    def get(self, id=None):
        if id:
            emp = db.session.query(Employee).get(id)
            if emp:
                db.session.delete(emp)
                db.session.commit()
        return redirect(url_for('.emp_list'))


class EmployeeCreateOrEditView(MethodView):
    def get(self, id=None):
        emp = Employee() if not id else db.session.query(Employee).get(id)
        form = EmployeeForm(request.form, obj=emp)
        form.department_id.choices = [(d.id, d.name) for d in Department.query.all()]
        form.gender.choices = [('男', '男'), ('女', '女')]
        return render_template('emp-detail.html', form=form)

    def post(self, id=None):
        form = EmployeeForm(request.form)
        emp = Employee() if not id else db.session.query(Employee).get(id)
        form.populate_obj(emp)
        if not id:
            db.session.add(emp)
        db.session.commit()
        return redirect(url_for('.emp_list'))
