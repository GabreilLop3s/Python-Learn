from model.biblioteca import Biblioteca
from itens.livro import Livro
from itens.revista import Revista


biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")


livro1 = Livro("1984", "George Orwell", 30.0, "0889899")

revista1 = Revista("National Geographic", "John Doe",15.0, "Quinta")




# biblioteca_cidade.alterna_estado()
# biblioteca_shopping.alterna_estado()

# biblioteca_cidade.receber_avaliacao("Marcos", 8)
# biblioteca_shopping.receber_avaliacao("Yuri", 5)

def main ():
    Biblioteca.listar_bibliotecas
    
        

if __name__ == "__main__":
    main()



























