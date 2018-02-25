from flask import Blueprint

employee = Blueprint('employee', __name__)

from personal.views import *

employee.add_url_rule('/list/', view_func=EmployeeListView.as_view('employee_list'))
