import _sqlite3 #DELETE

# 1 - Conectando no BD
conexao = _sqlite3.connect("Titulo.db")
cursor = conexao.cursor()


# 2 - exclusão de dados
id = (3,4)
cursor.execute(
    """
        DELETE FROM filmes 
        WHERE id in (?,?)
    """,
    id
)
conexao.commit()

print("Dados excluidos com sucesso")