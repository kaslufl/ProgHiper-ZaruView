class Categoria:

    def __init__(self, lista_videos, thumbnail_URL, titulo, descricao):
        self._lista_videos = lista_videos
        self._thumbnail_URL = thumbnail_URL
        self._titulo = titulo
        self._descricao = descricao

    def get_lista_videos(self):
        return self._lista_videos

    def get_thumbnail_URL(self):
        return self._thumbnail_URL

    def get_titulo(self):
        return self._titulo

    def get_descricao(self):
        return self._descricao