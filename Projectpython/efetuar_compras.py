import cadastro_cliente 
import listar_produtos
from gerenciar_estoque import atualizar_estoque
from produto import Produto
import getpass


# criação de variável para verificar login, se foi feito
cliente_logado = False

def efetuar_compras():
    #funcao global é usada para acessar uma variável dentro e fora do escopo
    global cliente_logado

    if not cliente_logado:
        print("Apenas clientes registrados podem efetuar compras.")
        login_cliente()
    if not cliente_logado:
            return  # Sai da função se o login não for bem-sucedido

    print("Bem-vindo à área de compras!")

    while True:
        print("1. Listar Produtos")
        print("2. Adicionar Produto ao Carrinho")
        print("3. Finalizar Compra")
        print("4. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_produtos.listar_produtos()
        elif opcao == '2':
            adicionar_ao_carrinho()
            
        elif opcao == '3':
            finalizar_compra()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def login_cliente():
    global cliente_logado
    print("Bem-vindo, cliente! Use seu usuário e senha:")

    while True:
        username = input("Digite o usuário: ")
        password = getpass.getpass("Digite sua senha: ")

        if cadastro_cliente.validar_usuario_senha(username, password):
            cliente_logado = True
            print("Login bem-sucedido.")
            break
        else:
            print("Usuário ou senha incorretos. Tente novamente.")

carrinho = []

def adicionar_ao_carrinho():
    
    codigo = input("Digite o código do produto que deseja adicionar ao carrinho: ")
    quantidade = int(input("Digite a quantidade desejada: "))
    
    produto_existente = False

    for produto in listar_produtos.listar_produtos():
        if produto.codigo == codigo:
            produto_existente = True
            if produto.estoque >= quantidade:
                carrinho.append((produto, quantidade))
                print(f"{quantidade} unidades de {produto.nome} adicionadas ao carrinho.")
                # produto.estoque -= quantidade -> Já diminui quando finaliza compra. Se colocar aqui vai reduzir 2x
            else:
                print(f"Quantidade insuficiente de {produto.nome} em estoque.")

    if not produto_existente:
        print("Código do produto não encontrado.")
        
def finalizar_compra():
    total = 0    

    print("Produtos comprados:")
    for produto, quantidade in carrinho:
        preco_unitario = float(produto.preco.split('R$')[1].replace(',', '.').strip())
        subtotal = preco_unitario * quantidade
        total += subtotal
        print(f"{produto.nome}: {quantidade} unidades - R$ {subtotal:.2f}")

        atualizar_estoque(produto.codigo, quantidade)  # Chama a função para atualizar o estoque

    print(f"Total a pagar: R$ {total:.2f}")

    confirmar = input("Deseja confirmar a compra? Digite 1 para sim ou 2 para não: ")
    if confirmar == "2":
        carrinho.clear()
        print("Compra cancelada. Itens removidos do carrinho.")
    elif confirmar != "1":
        print("Opção inválida.")