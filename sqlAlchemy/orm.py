from sqlalchemy import create_engine, Column, Integer, String, Float #create engine é usado para a conexao com o banco de dados

from sqlalchemy.ext.declarative import declarative_base #cria uma classe base da qual todas as suas classes de modelo (que representam tabelas) devem herdar. Essa base contém metadados que permitem que o SQLAlchemy saiba como mapear suas classes para tabelas no banco.

from sqlalchemy.orm import sessionmaker #cria uma classe base da qual todas as suas classes de modelo (que representam tabelas) devem herdar. Essa base contém metadados que permitem que o SQLAlchemy saiba como mapear suas classes para tabelas no banco.

engine = create_engine("sqlite:///banco.db", echo=True) #conexao
base = declarative_base() #base das classes

class Filme(base):
     __tablename__ = "filmes"
     id = Column (Integer, primary_key = True)
     nome = Column(String, nullable= False,)
     ano = Column(Integer, nullable=False)
     nota = Column(Float, nullable=False)

base.metadata.create_all(engine)

 #inserir dados 
def adcionar_filme(nome, ano, nota):
     Session = sessionmaker(bind=engine)
     session = Session()
     filme = Filme(nome=nome, ano=ano, nota=nota)
     session.add(filme)
     session.commit()
     session.close()
    
def atualiza_filme(id, nome=None, ano=None, nota=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        if nome is not None:
            filme.nome = nome
        if nota is not None:
            filme.nota = nota
        if ano is not None:
            filme.ano = ano
            
        session.commit()
    session.close()
    
#atualiza_filme(1, "Homem-Aranha", 2017, 9)

def excluir_filme(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        session.delete(filme)
    session.commit()
    session.close()
    
excluir_filme(1)








