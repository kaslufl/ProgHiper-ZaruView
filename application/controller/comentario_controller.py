from application import app
from flask import render_template, request
from application.model.entity.video import Video
from application.model.entity.categoria import Categoria
from application.model.entity.comentario import Comentario
from application import categoria_dao

@app.route("/inserir", methods=['POST'])
def comentario(video):
    autor = request.form['autor']
    conteudo = request.form['conteudo']
    comentario = Comentario(autor, conteudo)
    video.set_novo_comentario(comentario)
    comentario_lista = video.get_comentarios()
    return render_template("comentario.html", comentario_lista = comentario_lista)