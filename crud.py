from datetime import datetime # Import da Lib datetime para tratamente de data em log
import mysql.connector # Import da Lib do MySQL Connector para conexão com MySQL
import os # Import da Lib OS para manipulação e referenciação de arquivo 
from dotenv import load_dotenv # Import da Lib do Dot_Env usando o load_dotenv para resgatar dados do .env
load_dotenv() 



# Funcoes auxiliares
def GetDate():  # Resgata a hora atual e formata para o formato de banco
    now = datetime.now()
    db_date = now.strftime('%Y-%m-%d %H:%M:%S')
    return db_date







# CONEXAO
conexao = mysql.connector.connect(  
    host=str(os.environ['host']),  # Resgata do .env o host do mysql
    user=str(os.environ['user']),  # Resgata do .env o user do mysql
    password=str(os.environ['password']),  # Resgata do .env a senha do banco do mysql
    database=str(os.environ['database']),  # Resgata do .env o Schema usado no mysql
)
cursor = conexao.cursor()   # Cria um cursor por onde os comandos MySQL serão enviados


# CRUD
table = str(os.environ['nome_tabela']) # Resgata do .env o nome da tabela do mysql

def CREATE(nome_produto, valor, quantidade):
    comando = f"SELECT * FROM {table} WHERE Nome_Produto = '{nome_produto}'"
    cursor.execute(comando)
    response = cursor.fetchall() # Quando armazenar algum resultado lido no banco de dados
    if response:
        quant_banco = response[0][3]
        quantidade = int(quantidade) + int(quant_banco)
        return UPDATE(nome_produto, valor, quantidade)
   
    try:
        agora = GetDate()
        comando = f"INSERT INTO {table} (nome_produto, valor, quantidade, Data_Atualizacao) VALUES ('{nome_produto}', {valor}, {quantidade}, '{agora}')"
        cursor.execute(comando)
        conexao.commit() # Quando editar algumas informação no banco de dados
    except TypeError:
        print('Erro ao adicionar, por favor verifique se colocou o nome do produto e o novo valor corretamente(Sem "R$")')


def READ():
    comando = f'SELECT * FROM {table}'
    cursor.execute(comando)
    response = cursor.fetchall() # Quando armazenar algum resultado lido no banco de dados
    return response


def UPDATE(nome_produto, valor=None, quantidade=None):
    try:
        agora = GetDate()

        # Altera o Update para cada necessidade de alteração das linhas
        if valor != None and quantidade == None:
            comando = f"UPDATE {table} SET Valor = {valor}, Data_Atualizacao = '{agora}' WHERE nome_produto = '{nome_produto}'"
        
        elif valor == None and quantidade !=None:
            comando = f"UPDATE {table} SET Quantidade = {quantidade}, Data_Atualizacao = '{agora}' WHERE nome_produto = '{nome_produto}'"
        
        elif valor and quantidade:
            comando = f"UPDATE {table} SET Valor = {valor}, Quantidade = {quantidade}, Data_Atualizacao = '{agora}' WHERE nome_produto = '{nome_produto}'"

        elif not valor and not quantidade:
            print('Operacao invalida - Valores vazios')
            return 


        cursor.execute(comando)
        conexao.commit() # Quando editar algumas informação no banco de dados

    except TypeError:
        print('Erro ao editar, por favor verifique se colocou o nome do produto e o novo valor corretamente(Sem "R$")')
    except Exception as erro:
        erro = str(erro)
        id_erro = erro.split(' ')[0]
        if id_erro == '1064':
            print(f'Erro ao atualizar {nome_produto} - produto inexistente!')
        else:
            print(erro)


def DELETE(nome_produto):
    try:
        comando = f"DELETE FROM {table} WHERE nome_produto = '{nome_produto}'"
        cursor.execute(comando)
        conexao.commit() # Quando editar algumas informação no banco de dados
    except TypeError:
        print('Erro ao Deletar, por favor verifique se colocou o nome do produto corretamente')



#CREATE(nome_produto='Toddynho', valor=3.5, quantidade=300)
#UPDATE(nome_produto='Toddynho', valor=3.5)
#print(READ())
#DELETE('Toddynho')




# Encerra a coneção com o banco (IMPORTANTE NÃO ESQUECER)
cursor.close()
conexao.close()