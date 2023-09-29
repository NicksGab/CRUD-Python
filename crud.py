import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

conexao = mysql.connector.connect(
    host=str(os.environ['host']),
    user=str(os.environ['user']),
    password=str(os.environ['password']),
    database=str(os.environ['database']),
)


cursor = conexao.cursor()

# CRUD

def CREATE():
    nome_produto = 'Toddynho'
    valor = 3.5
    quantidade = 300
    comando = f"INSERT INTO vendas (nome_produto, valor, quantidade) VALUES ('{nome_produto}', {valor}, {quantidade})"
    cursor.execute(comando)
    conexao.commit() # Quando editar algumas informação no banco de dados



def READ():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    result = cursor.fetchall() # Quando armazenar algum resultado lido no banco de dados
    print(result)


def UPDATE():
    nome_produto = 'Toddynho'
    valor = 6
    comando = f"UPDATE vendas SET valor = {valor} WHERE nome_produto = '{nome_produto}'"
    cursor.execute(comando)
    conexao.commit() # Quando editar algumas informação no banco de dados

def DELETE():
    nome_produto = 'Toddynho'
    comando = f"DELETE FROM vendas WHERE nome_produto = '{nome_produto}'"
    cursor.execute(comando)
    conexao.commit() # Quando editar algumas informação no banco de dados


#CREATE()
#READ()
#UPDATE()
#DELETE()



cursor.close()
conexao.close()