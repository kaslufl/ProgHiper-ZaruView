from application import app
from flask import render_template, request
from application.model.entity.video import Video
from application.model.entity.categoria import Categoria
from application.model.entity.comentario import Comentario
from application import categoria_dao

@app.route("/categoria/<categoria_id>/video/<id>")
def video(categoria_id, id):
    video = categoria_dao.get_video_by_id(int(id))
    comentario_lista = video.get_categoria_titulo()
    return render_template("video.html", video = video, comentario_lista = comentario_lista)
