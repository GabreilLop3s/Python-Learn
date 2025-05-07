import sqlite3 #CREATE

conexao = sqlite3.connect('Titulo.db')
cursor = conexao.cursor()

#PASSO 3 - INSERÇÃO DOS DADOS

cursor.execute( #cursor age como uma ponte entre o banco de dados e a IDE, como se você ligasse pra alguem o snal passa por algo antes de ser direcionado pra pessoa que deseja ligar
    """
            INSERT INTO filmes(nome, ano, nota)
            VALUES('Mario',2021, 8.5)
        
    
    """
)

conexao.commit()
conexao.close()
print("Dados inseridos com sucesso")






































