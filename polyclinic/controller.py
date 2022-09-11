from flask_sqlalchemy import SQLAlchemy as alchemy

class Poly():
    def __init__(self):
        self.db = SQLAlchemy(app)


