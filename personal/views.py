from flask import render_template, redirect, url_for, request
from flask.views import MethodView
from pms import db
from .models import Employee, Department


class EmployeeListView(MethodView):
    def get(self):
        items = db.session.query(Employee).all()[:10]
        return render_template('emp-list.html', items=items)


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
        from personal.forms import EmployeeForm
        form = EmployeeForm()
        # departments = db.session.query(Department).all()
        return render_template('emp-detail.html', form=form)

    def post(self, id=None):
        pass
