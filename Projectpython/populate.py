import sqlite3

#criação de tabelas e inserção de dados nessa tabela

try:
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

   #caso não exista
    cursor.execute('''CREATE TABLE IF NOT EXISTS administrador (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL
                    )''')
    # Inserir
    sql = 'INSERT INTO administrador (username, password) VALUES (?, ?)'
    cursor.execute(sql, ['Admin_1', 'Minha Senha'])
    conn.commit()

    print("Inserção bem-sucedida.")

except sqlite3.Error as e:
    print(f"Erro: {e}")

finally:
    conn.close()


#deletar tabela
'''def deletar_tabela(administrador):
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    try:
        cursor.execute(f"DROP TABLE IF EXISTS {administrador}")
        print(f"Tabela '{administrador}' deletada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao deletar tabela: {e}")

    conn.commit()
    conn.close()'''