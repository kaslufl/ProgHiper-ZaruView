from application import app
from flask import render_template, request
from application.model.entity.video import Video
from application.model.entity.categoria import Categoria
from application.model.entity.comentario import Comentario
from application import categoria_dao


@app.route("/categoria/<id>")
def categoria(id):
    categoria = categoria_dao.get_categoria_by_id(int(id))

    return render_template("categoria.html", categoria = categoria)