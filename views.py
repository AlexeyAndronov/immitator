from app import app
from flask import render_template, url_for
from flask.views import View
from catalogController import CatalogController
from models import Catalog

class CatalogView(View):
    def dispatch_request(self):
        t = Catalog.query.all()
        print (t)
        return render_template('index.html', context=t)

    def __init__(self):
        self.cat = CatalogController()


app.add_url_rule('/', view_func=CatalogView.as_view("index"))