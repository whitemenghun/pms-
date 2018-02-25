from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from personal import employee

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/pms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

app.register_blueprint(employee, url_prefix='/emp')


@app.route('/')
def index():
    return 'index!'

@app.route('/admin/emp/list/')
def admin_emp_list():
    return render_template('admin/emp-list.html')


if __name__ == '__main__':
    app.run(debug=True)
