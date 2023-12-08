import sqlite3
import registrar

#consulta a valores de uma tabela e alteração de senha e usuários

conn = sqlite3.connect('db.sqlite') # Conectar ao banco de dados
cursor = conn.cursor()

sql = 'SELECT * FROM clientes' # Executar uma consulta
cursor.execute(sql)

results = cursor.fetchall() # Recuperar os resultados

for row in results: # Exibir os resultados
    print(row)
conn.close() # Fechar a conexão'''


'''def alterar_senha(username, password):
    try:
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()

        # UPDATE == alteração
        sql = 'UPDATE users SET password = ? WHERE username = ?'
        cursor.execute(sql, (password, username))
        
        conn.commit()
        print("Senha alterada com sucesso.")

    except sqlite3.Error as e:
        print(f"Erro: {e}")

    finally:
        # Fechar a conexão
        conn.close()'''




