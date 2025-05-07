import sqlite3 

# 1 - conectando no bd

def conecta_bd():
    conexao = sqlite3.connect("Titulo.db")
    return conexao

# 2 - inserir dados
def inserir_dados(nome, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
    """
        INSERT INTO filmes(nome, ano, nota)
        VALUES(?, ?, ?)
    """,
    (nome, ano, nota)
    )
    conexao.commit()
    conexao.close()
    
# 3 - Listagem de dados
def obter_dados():
    conexao = conecta_bd()
    cursor =  conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    cursor.close()
    return dados 

# 4 - excluir dados
def excluir_dados(id):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
        '''
        DELETE FROM filmes
        WHERE id = ?
        ''',
        (id,)
    )
    conexao.commit()
    conexao.close()

    