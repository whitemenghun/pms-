from flask import Blueprint

employee = Blueprint('employee', __name__)

from personal.views import *

employee_list_view = EmployeeListView.as_view('emp_list')

employee.add_url_rule('/list/', view_func=employee_list_view, defaults={'page': 1})
employee.add_url_rule('/list/<int:page>', view_func=employee_list_view)
employee.add_url_rule('/del/<int:id>/', view_func=EmployeeDelView.as_view('emp_del'))
employee.add_url_rule('/create/', view_func=EmployeeCreateOrEditView.as_view('emp_create'))
employee.add_url_rule('/edit/<int:id>/', view_func=EmployeeCreateOrEditView.as_view('emp_edit'))
