
from model.avaliacao import Avaliacao
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Biblioteca:
    bibliotecas = []
    def __init__(self, nome):
        self.nome = nome 
        self._ativo = False
        self._avaliacao = []
        Biblioteca.bibliotecas.append(self)
        
    
    def __str__(self):
        return self.nome
    
    
    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'nome da biblioteca'.ljust(25)} | {'Nota media'.ljust(25)} | {'Status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {str(biblioteca.media_avaliacoes.ljust(25))} |{biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo
    
    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"
    
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        
    @property 
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum( avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao)), 1  
        return media
        
        
    



























