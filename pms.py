from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from personal import employee

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/pms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key= 'asdiojasidojasd'

db = SQLAlchemy(app)

app.register_blueprint(employee, url_prefix='/emp')


@app.route('/')
def index():
    return 'index!'


if __name__ == '__main__':
    app.run(debug=True)
