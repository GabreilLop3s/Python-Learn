import sqlite3 # READ

conexao = sqlite3.connect('Titulo.db')
cursor = conexao.cursor()

#Leitura de dados
dados = cursor.execute("SELECT * FROM filmes")

print (dados)