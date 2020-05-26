from application import app
from flask import render_template

@app.route("/")
@app.route("/home")
def helllo():
    return render_template("home.html")