from application import app
from flask import render_template, request
from application.model.entity.video import Video
from application.model.entity.categoria import Categoria
from application.model.dao.categoria_dao import CategoriaDAO


@app.route("/categoria/<id>")
def categoria(id):
    return render_template("categoria.html")