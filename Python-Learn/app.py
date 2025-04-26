from model.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")

biblioteca_cidade.alterna_estado()
biblioteca_shopping.alterna_estado()

biblioteca_cidade.receber_avaliacao("Marcos", 8)
biblioteca_shopping.receber_avaliacao("Yuri", 5)

def main ():
    Biblioteca.listar_bibliotecas
    
        

if __name__ == "__main__":
    main()



























