from application.model.entity.categoria import Categoria
from application.model.entity.video import Video
from datetime import date


class CategoriaDAO:

    def __init__(self):
        video_A00 = Video("video_URl", "images/ZV.png", "a", "descricao", date(2020, 5, 28), 1)
        video_A01 = Video("video_URl", "images/ZV.png", "b", "descricao", date(2020, 5, 28), 2)
        video_B00 = Video("video_URl", "images/ZV.png", "c", "descricao", date(2020, 5, 28), 3)
        video_B01 = Video("video_URl", "images/ZV.png", "d", "descricao", date(2020, 5, 28), 4)
        video_C00 = Video("video_URl", "images/ZV.png", "e", "descricao", date(2020, 5, 28), 5)
        video_C01 = Video("video_URl", "images/ZV.png", "f", "descricao", date(2020, 5, 28), 6)

        self._todos_videos = [video_A00, video_A01, video_B00, video_B01, video_C00, video_C01]

        self._categoria_list = []
        self._categoria_list.append(Categoria([video_A00, video_A01], "images/ZV.png", "titulo", "descricao", 1))

        self._categoria_list.append(Categoria([video_B00, video_B01], "images/ZV.png", "titulo", "descricao", 2))

        self._categoria_list.append(Categoria([video_C00, video_C01], "images/ZV.png", "titulo", "descricao", 3))

    def listar_todos_categoria(self):
        return self._categoria_list

    def listar_todos_videos(self):
        return self._todos_videos