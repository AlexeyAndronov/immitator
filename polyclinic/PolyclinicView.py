from app import app
from flask import render_template, url_for
from flask.views import View

class PolyclinicView(View):
    def dispatch_request(self):
        vars = {}
        return render_template("polyclinic.html", context = vars)


app.add_url_rule('/polyclinic/', view_func=PolyclinicView.as_view("poly"))