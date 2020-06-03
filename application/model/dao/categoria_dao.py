from application.model.entity.categoria import Categoria
from application.model.entity.video import Video
from datetime import date


class CategoriaDAO:

    def __init__(self):
        categoria1 = Categoria("images/ZV.png","Cat1","descricao",1) 
        categoria2 = Categoria("images/ZV.png","Cat2","descricao",2)
        categoria3 = Categoria("images/ZV.png","Cat3","descricao",3)

        video_A00 = Video("video_URL", "images/ZV.png", "a", "descricao", date(2020, 5, 28), categoria1, 1)
        video_A01 = Video("video_URL", "images/ZV.png", "b", "descricao", date(2020, 5, 28), categoria1, 2)
        video_B00 = Video("video_URL", "images/ZV.png", "c", "descricao", date(2020, 5, 28), categoria2, 3)
        video_B01 = Video("video_URL", "images/ZV.png", "d", "descricao", date(2020, 5, 28), categoria2, 4)
        video_C00 = Video("video_URL", "images/ZV.png", "e", "descricao", date(2020, 5, 28), categoria3, 5)
        video_C01 = Video("video_URL", "images/ZV.png", "f", "descricao", date(2020, 5, 28), categoria3, 6)

        self._todos_videos = [video_A00, video_A01, video_B00, video_B01, video_C00, video_C01]
        
        categoria1.set_video(video_A00)
        categoria1.set_video(video_A01)
        categoria2.set_video(video_B00)
        categoria2.set_video(video_B01)
        categoria3.set_video(video_C00)
        categoria3.set_video(video_C01)
        

        self._categoria_list = []
        
        self._categoria_list.append(categoria1)

        self._categoria_list.append(categoria2)

        self._categoria_list.append(categoria3)

    def listar_todos_categoria(self):
        return self._categoria_list

    def listar_todos_videos(self):
        return self._todos_videos