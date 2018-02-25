from flask import Blueprint

employee = Blueprint('employee', __name__)

from personal.views import *

employee.add_url_rule('/list/', view_func=EmployeeListView.as_view('emp_list'))
employee.add_url_rule('/del/<int:id>/', view_func=EmployeeDelView.as_view('emp_del'))
employee.add_url_rule('/create/', view_func=EmployeeCreateOrEditView.as_view('emp_create'))
employee.add_url_rule('/edit/<int:id>/', view_func=EmployeeCreateOrEditView.as_view('emp_edit'))
