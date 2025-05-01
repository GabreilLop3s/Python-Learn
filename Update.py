import _sqlite3 #UPDATE

# 1 - Conectando no BD
conexao = _sqlite3.connect("Titulo.db")
cursor = conexao.cursor()

# 2 - Atualizando Dados
# passamos o id 
id = 1

#Lembradno q o crusor é como se fosse uma ponte para executar as tarefas, então executamos o cursor.
cursor.execute(
    """
        UPDATE filmes SET nota = ?
        WHERE id = ?
    """,
    (10, id)
)
conexao.commit()

print ("Dados Atualizados")




