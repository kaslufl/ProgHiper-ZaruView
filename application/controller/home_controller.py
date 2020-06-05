from application import app
from flask import render_template, request
from application.model.entity.video import Video
from application.model.entity.categoria import Categoria
from application.model.entity.comentario import Comentario
from application import categoria_dao



@app.route("/")
@app.route("/home")
def home():
    videos_mais_curtidos = sorted(categoria_dao.listar_todos_videos(), key=Video.get_curtidas, reverse=True)
    lista_categorias = categoria_dao.listar_todos_categoria()
    return render_template("home.html", videos_mais_curtidos = videos_mais_curtidos, lista_categorias = lista_categorias)

