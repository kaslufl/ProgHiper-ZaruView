from application.model.entity.categoria import Categoria
from application.model.entity.video import Video
from datetime import date


class CategoriaDAO:

    def __init__(self):
        video_A00 = Video("video_URl", "thumbnail_URL", "a", "descricao", date(2020, 5, 28), 1)
        video_A01 = Video("video_URl", "thumbnail_URL", "b", "descricao", date(2020, 5, 28), 2)
        video_B00 = Video("video_URl", "thumbnail_URL", "c", "descricao", date(2020, 5, 28), 3)
        video_B01 = Video("video_URl", "thumbnail_URL", "d", "descricao", date(2020, 5, 28), 4)
        video_C00 = Video("video_URl", "thumbnail_URL", "e", "descricao", date(2020, 5, 28), 5)
        video_C01 = Video("video_URl", "thumbnail_URL", "f", "descricao", date(2020, 5, 28), 6)

        self._categoria_list = []
        self._categoria_list.append(Categoria([video_A00, video_A01], "thumbnail_URL", "titulo", "descricao"))

        self._categoria_list.append(Categoria([video_B00, video_B01], "thumbnail_URL", "titulo", "descricao"))

        self._categoria_list.append(Categoria([video_C00, video_C01], "thumbnail_URL", "titulo", "descricao"))

    def listar_todos(self):
        return self._categoria_list

