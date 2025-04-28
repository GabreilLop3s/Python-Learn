import sqlite3

conexao = sqlite3.connect('Titulo.db')
cursor = conexao.cursor()

cursor.execute(
    """
            INSERT INTO filmes(nome, ano, nota)
            VALUES('Sonic',2020, 8.0)
    
    """
)

conexao.commit()
conexao.close()
print("Dados inseridos com sucesso")


































