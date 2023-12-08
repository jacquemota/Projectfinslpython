from listar_produtos import lista_produtos
import sqlite3
from datetime import datetime
import main as main

class Produto:
    def __init__(self, codigo, nome, marca, data_validade, preco, estoque):
        self.codigo = codigo
        self.nome = nome
        self.marca = marca
        self.data_validade = data_validade
        self.preco = preco
        self.estoque = estoque

print("Bem-vindo à área de gerenciamento de estoque")


def adicionar_estoque():
    # Lógica para adicionar itens ao estoque (apenas administrador)
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()

    # criar tabela produtos se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT(50),
            marca TEXT(50),
            data_validade DATE,
            preco FLOAT,
            estoque INTEGER
        )
    ''')

    # Salvar as alterações
    conn.commit()

    # Inserir na tabela
    try:
        novo_Produto = _extracted_from_adicionar_estoque_23(cursor)
        print("Produto adicionado com sucesso.")

    except ValueError as e:
        print(f"Erro: {e}")

    # Salvar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()

# função de adicionar ao estoque
def _extracted_from_adicionar_estoque_23(cursor):
    nome = input("Digite o nome do produto: ")
    marca = input("Digite a marca do produto: ")
    data_validade = input("Digite a data de validade do produto (YYYY-MM-DD): ")

    # Convertendo a data para o formato correto
    try:
        data_validade = datetime.strptime(data_validade, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Formato de data inválido. Use o formato YYYY-MM-DD.")

    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade a ser adicionada:"))

    novo_produto = Produto(nome, marca, data_validade, preco, estoque)
    
    # Inserir os dados na tabela
    cursor.execute('''
        INSERT INTO produtos (nome, marca, data_validade, preco, estoque)
        VALUES (?, ?, ?, ?, ?)
    ''', (novo_produto.nome, novo_produto.marca, novo_produto.data_validade,
        novo_produto.preco, novo_produto.estoque))

    return novo_produto

# Chamando a função
adicionar_estoque()


while True:
    print("1. Ver estoque de produtos")
    print("2. Adicionar itens no estoque")
    print("3. Excluir itens no estoque")
    print("4. Voltar ao Menu Principal")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        lista_produtos.listar_produtos()
    elif opcao == '2':
        adicionar_estoque()
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")