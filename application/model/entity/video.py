from application.model.entity import categoria
class Video:

    def __init__(self, video_URL, thumbnail_URL, titulo, descricao, data_publicacao, categoria, codigo): 
        self._video_URL = video_URL 
        self._thumbnail_URL = thumbnail_URL
        self._titulo = titulo
        self._descricao = descricao
        self._data_publicacao = data_publicacao
        self._categoria = categoria
        self._id = codigo
        self._visualizacoes = 0
        self._curtidas = 0
        self._comentarios = []
    
    def get_video_URL(self):
        return self._video_URL
    
    def get_thumbnail_URL(self):
        return self._thumbnail_URL
    
    def get_titulo(self):
        return self._titulo
    
    def get_descricao(self):
        return self._descricao
    
    def get_data_publicacao(self):
        return self._data_publicacao

    def get_categoria_titulo(self):
        return self._categoria.get_titulo()

    def get_categoria_id(self):
        return self._categoria.get_id()

    def get_id(self):
        return self._id

    def get_visualizacoes(self):
        return self._visualizacoes

    def get_curtidas(self):
        return self._curtidas

    def get_comentarios(self):
        return self._comentarios

    class Comentario:
        
        def __init__(self, autor, conteudo, data_publicacao):
            self._autor = autor
            self._conteudo = conteudo
            self._data_publicacao = data_publicacao

        def get_autor(self):
            return self._autor

        def get_conteudo(self):
            return self._conteudo

        def get_data_publicacao(self):
            return self._data_publicacao