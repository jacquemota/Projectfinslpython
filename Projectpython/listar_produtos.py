from produto import Produto

# Exemplo de lista de produtos
lista_produtos = [
    Produto("001", "Arroz", "Urbano", "2024-12-31","R$ 4,00", 50),
    Produto("002", "Biscoito", "Treloso", "2025-06-30", "R$ 2,00", 30),
    Produto("003", "Bolacha", "Macrilan", "2024-08-30", "R$ 5,00", 10)
    
]

def listar_produtos():
    for produto in lista_produtos:
        print(f"Código: {produto.codigo}")
        print(f"Nome: {produto.nome}")
        print(f"Marca: {produto.marca}")
        print(f"Data de Validade: {produto.data_validade}")
        print(f"preco: {produto.preco}")
        print(f"Estoque: {produto.estoque}")
        print("------------")

    return lista_produtos
