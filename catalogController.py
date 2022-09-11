from app import app
from app import db
from flask_sqlalchemy import SQLAlchemy
from models import Catalog

class CatalogController():
    def __init__(self):
        print ("init")
        self.db = db

    def getCatalogue(self):
        print ("getCatalog")
        result = Catalog.query.all()
        print (f"Catalog = {result}")
        return result