from application.model.entity.categoria import Categoria
from application.model.entity.video import Video
from datetime import date

class CategoriaDAO:

    def __init__(self):
        categoria1 = Categoria("images/thumb_league.png","League of Legends","Vídeos sobre League of Legends",1) 
        categoria2 = Categoria("images/thumb_runeterra.png","Legends of Runeterra","Vídeos sobre Legends of Runeterra",2)
        categoria3 = Categoria("images/thumb_witcher.png","The Witcher 3","Vídeos sobre The Witcher 3",3)

        video_A00 = Video("videos/league_1.mp4", "images/thumb_league_1.png", "Flash + Q do Bardo", "League of Legends", date(2020, 5, 28), categoria1, 1)
        video_A01 = Video("videos/league_2.mp4", "images/thumb_league_2.png", "Akali Rulada", "League of Legends", date(2020, 5, 28), categoria1, 2)
        video_B00 = Video("videos/runeterra_1.mp4", "images/thumb_runeterra_1.png", "Rex Correnteza", "Legends of Runeterra", date(2020, 5, 28), categoria2, 3)
        video_B01 = Video("videos/runeterra_2.mp4", "images/thumb_runeterra_2.png", "Julgamento Neles", "Legends of Runeterra", date(2020, 5, 28), categoria2, 4)
        video_C00 = Video("videos/witcher_1.mp4", "images/thumb_witcher_1.png", "Anoitecer ft. Carpeado", "The Witcher 3", date(2020, 5, 28), categoria3, 5)
        video_C01 = Video("videos/witcher_2.mp4", "images/thumb_witcher_2.png", "Tutorial TW3", "The Witcher 3", date(2020, 5, 28), categoria3, 6)
        
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
    
    def get_video_by_id(self, id):
        video_list = list(filter(lambda video : video.get_id() == id, self._todos_videos))
        if len(video_list) == 0:
            return None
        return video_list[0] 

    def get_categoria_by_id(self, id):
        categoria_list = list(filter(lambda categoria : categoria.get_id() == id, self._categoria_list))
        if len(categoria_list) == 0:
            return None
        return categoria_list[0] 
    
    def get_video_by_titulo(self, titulo):
        video_list = list(filter(lambda video : video.get_titulo() == titulo, self._todos_videos))
        if len(video_list) == 0:
            return None
        return video_list[0] 