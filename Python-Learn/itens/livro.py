from itens.livro import itemBibliioteca

class Livro(itemBibliioteca):
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco, isbn)
        self.isbn = isbn
        
    
        