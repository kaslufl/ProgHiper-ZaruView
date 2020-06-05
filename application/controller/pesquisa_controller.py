from application import app
from flask import render_template, request
from application.model.entity.video import Video
from application.model.entity.categoria import Categoria
from application.model.entity.comentario import Comentario
from application import categoria_dao

@app.route("/pesquisa")
def pesquisa():
    video_titulo = request.args.get('titulo')
    video = categoria_dao.get_video_by_titulo(video_titulo)
    return render_template("pesquisa.html", video = video)