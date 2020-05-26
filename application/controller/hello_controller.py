from application import app
from flask import render_template

@app.route("/")
def helllo():
    return render_template("index.html")