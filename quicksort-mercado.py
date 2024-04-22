class Produto:
    def __init__(self, nome, preco, quantidade, popularidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.popularidade = popularidade
    
    def __repr__(self):
        return f"Produto({self.nome}, R${self.preco}, {self.quantidade} unidades, Popularidade: {self.popularidade})"

def quick_sort_produtos(produtos, chave):
    if len(produtos) <= 1:
        return produtos

    pivot = getattr(produtos[len(produtos) // 2], chave)
    left = [x for x in produtos if getattr(x, chave) < pivot]
    middle = [x for x in produtos if getattr(x, chave) == pivot]
    right = [x for x in produtos if getattr(x, chave) > pivot]

    return quick_sort_produtos(left, chave) + middle + quick_sort_produtos(right, chave)

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque do produto: "))
    popularidade = int(input("Digite a popularidade do produto: "))
    return Produto(nome, preco, quantidade, popularidade)

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
                criterio = input("Digite o critério de ordenação (preco, quantidade, popularidade): ").lower()
                produtos_ordenados = quick_sort_produtos(produtos, criterio)
                print(f"\nProdutos (ordenados por {criterio}):")
                for produto in produtos_ordenados:
                    print(produto)
        elif opcao == '3':
            print("Obrigado por usar nosso sistema! Até mais.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
