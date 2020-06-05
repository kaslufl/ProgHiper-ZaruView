class Comentario:
    
    def __init__(self, autor, conteudo):
        self._autor = autor
        self._conteudo = conteudo

    def get_autor(self):
        return self._autor

    def get_conteudo(self):
        return self._conteudo
