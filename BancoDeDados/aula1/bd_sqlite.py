import sqlite3

conexao = sqlite3.connect('basededados.db') #Criando conexão
cursor =conexao.cursor()

#cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#               'nome TEXT,'
#               'peso REAL'
#               ')') #Criando tabela

#cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Matheus Sena", 55.5)') #Inserindo dados
#conexao.commit() #Executando comando

cursor.execute('SELECT * FROM clientes') #Consultando dados

for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)

cursor.close()
conexao.close() #Fechando cursor e conexao