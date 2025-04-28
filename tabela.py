import sqlite3

conexao =  sqlite3.connect('Titulo.db')

#criando cursor
cursor = conexao.cursor()

# criando a tabela
cursor.execute(
    """
        CREATE TABLE filmes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        
        );
    """
)

#fecha a conexao
conexao.close()
print("Tabela foi criada")

