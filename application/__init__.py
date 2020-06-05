from flask import Flask
import os
from application.model.dao.categoria_dao import CategoriaDAO

categoria_dao = CategoriaDAO()

app = Flask(__name__,
static_folder = os.path.abspath("application/view/static"),
template_folder = os.path.abspath("application/view/templates"))

from application.controller import home_controller
from application.controller import video_controller
from application.controller import categoria_controller
from application.controller import pesquisa_controller
from application.controller import comentario_controller
 