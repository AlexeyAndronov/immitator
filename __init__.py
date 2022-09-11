from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://djuser:djpassword@localhost:5433/bsc_immitator'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'e62a8461-db4f-40fa-93cf-404d93d66e9f'
db = SQLAlchemy(app)

from app import views
