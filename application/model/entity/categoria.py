class Categoria:

    def __init__(self, thumbnail_URL, titulo, descricao, codigo):
        self._lista_videos = []
        self._thumbnail_URL = thumbnail_URL
        self._titulo = titulo
        self._descricao = descricao
        self._id = codigo

    def get_lista_videos(self):
        return self._lista_videos

    def get_thumbnail_URL(self):
        return self._thumbnail_URL

    def get_titulo(self):
        return self._titulo

    def get_descricao(self):
        return self._descricao

    def get_id(self):
        return self._id
    
    def set_video(self, video):
        self._lista_videos.append(video)