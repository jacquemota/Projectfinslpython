import sqlite3
import cadastro_cliente
import cadastro_admin
import getpass


def criar_tabela_clientes():
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL,
            endereco TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def cadastrar_cliente():

    while True:
        nome = input("Digite o nome completo: ")
        email = input("Digite o email: ")
        usuario = input("Digite o usuário: ")
        senha = getpass.getpass("Digite a senha: ")
        endereco = input("Digite o endereço: ")

        if '@' not in email:
            print("Email inválido. O email deve conter '@'.")
            continue

        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()

        try:
            cursor.execute(
    "INSERT INTO clientes (nome, email, usuario, senha, endereco) VALUES (?, ?, ?, ?, ?)",
    (nome, email, usuario, senha, endereco)
)
            
            print("Cadastro de cliente realizado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao cadastrar cliente: {e}")

        finally:
            conn.commit()
            conn.close()
            break

def criar_tabela_administradores():
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS administradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def cadastrar_admin():
    
    while True:
        nome = input("Digite o nome completo: ")
        email = input("Digite o email: ")
        usuario = input("Digite o usuário: ")
        senha = getpass.getpass("Digite a senha: ")
        endereco = input("Digite o endereço: ")

        if '@' not in email:
            print("Email inválido. O email deve conter '@'.")
            continue

        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()

        try:
            cursor.execute(
    "INSERT INTO admin (nome, email, usuario, senha, endereco) VALUES (?, ?, ?, ?, ?)",
    (nome, email, usuario, senha, endereco)
)
            print("Cadastro de administrador realizado com sucesso!")

        except sqlite3.Error as e:
            print(f"Erro ao cadastrar administrador: {e}")

        finally:
            conn.commit()
            conn.close()
            break

    
    

def registrar():
    print("Opções de Registro:")
    print("1. Cliente")
    print("2. Administrador")
    print("3. Alterar dados de cadastro")
    opcao = input("Escolha uma opção de registro: ")
    
    if opcao == '1':
        cadastrar_cliente()
    elif opcao == '2':
        cadastrar_admin()  
    elif opcao == '3':
        print("você é cliente ou um administrador?")
        opcao = input("Digite 1 para cliente ou 2 para administrador:")
        
        
        

