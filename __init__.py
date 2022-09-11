from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from const import sc_key, user, passwd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{passwd}@localhost:5433/bsc_immitator'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = sc_key
db = SQLAlchemy(app)

from app import views
