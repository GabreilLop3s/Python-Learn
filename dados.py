import sqlite3

conexao = sqlite3.connect('Titulo.db')
cursor = conexao.cursor()

cursor.execute( #cursor age como uma ponte entre o banco de dados e a IDE, como se você ligasse pra alguem o snal passa por algo antes de ser direcionado pra pessoa que deseja ligar
    """
            INSERT INTO filmes(nome, ano, nota)
            VALUES('Sonic',2020, 8.0)
    
    """
)

conexao.commit()
conexao.close()
print("Dados inseridos com sucesso")






































