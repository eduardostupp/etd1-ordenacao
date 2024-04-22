class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def __repr__(self):
        return f"Produto({self.nome}, R${self.preco}, {self.quantidade} unidades)"

def quick_sort_produtos(produtos):
    if len(produtos) <= 1:
        return produtos

    pivot = produtos[len(produtos) // 2].quantidade
    left = [x for x in produtos if x.quantidade > pivot]
    middle = [x for x in produtos if x.quantidade == pivot]
    right = [x for x in produtos if x.quantidade < pivot]

    return quick_sort_produtos(left) + middle + quick_sort_produtos(right)

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque do produto: "))
    return Produto(nome, preco, quantidade)

def main():
    produtos = []

    print("Bem-vindo ao sistema de gerenciamento de estoque!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar produto")
        print("2. Ver produtos ordenados")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            produto = adicionar_produto()
            produtos.append(produto)
            print("Produto adicionado com sucesso!")
        elif opcao == '2':
            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                produtos_ordenados = quick_sort_produtos(produtos)
                print("\nProdutos (ordenados por quantidade):")
                for produto in produtos_ordenados:
                    print(produto)
        elif opcao == '3':
            print("Obrigado por usar nosso sistema! Até mais.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
