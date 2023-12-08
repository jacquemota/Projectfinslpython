import sqlite3
import efetuar_compras as efetuar_compras


def verificar_nome(nome): # Verifique se o nome não contém caracteres iguais
    if len(set(nome.replace(' ', ''))) > 1:
        return True 
    

    nome_estranho = ["sim", "não"] #Verifique se o nome está na lista de nomes estranhos
    if nome.lower() in nome_estranho:
        return nome.lower() not in nome_estranho

def verificar_email(email): #Verifique se o email contém '@'
        return '@' in email
    

def verificar_endereco(endereco):
    return endereco.lower() == 'cliente'

def login_cliente(username, password):
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    sql = "SELECT * FROM users WHERE username=? AND password=?"
    return cursor.execute(sql, [username, password]).fetchone()


