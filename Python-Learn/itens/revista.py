from itens.revista import itemBibliioteca

class Revista(itemBibliioteca):
    def __init__(self, titulo, autor, preco, edicao):
        super().__init__(titulo, autor, preco)
        self.edicao = edicao
        