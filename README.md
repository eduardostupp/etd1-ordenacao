# Métodos de Classificação e Ordenação

 - ### Estrutura de Dados I
 - __Alunos__: Eduardo Stupp e Lucas Eduardo Mendonça
 - __Professor__: Fernando Bastos

Neste documento, discutiremos os métodos de classificação internos e externos, além de apresentar uma breve explicação e análise dos seguintes algoritmos de ordenação:

1. [MergeSort](#mergesort)
2. [QuickSort](#quicksort)
3. [Selection Sort](#selection-sort)
4. [Insertion Sort](#insertion-sort)

## Métodos de Classificação

### Classificação Interna

Métodos de classificação interna são algoritmos que organizam elementos de uma lista ou array dentro da própria estrutura de dados. Eles são muito bom para conjuntos de dados que podem ser completamente carregados na memória principal do computador. Exemplos incluem algoritmos como Quicksort, Mergesort, Insertion Sort e Selection Sort, que vamos estar apresentando no documento abaiuxo.

### Classificação Externa

Métodos de classificação externa são usados quando os dados não podem ser completamente carregados na memória principal do computador devido ao seu tamanho, prejudicando o funcionamento do código. Esses algoritmos usam estratégias de ordenação que envolvem a leitura e escrita de blocos de dados para armazenamento temporário em disco. Exemplos incluem algoritmos como o Merge Sort externo.

## Métodos de Ordenação

## [MergeSort](#mergesort)

O MergeSort é um algoritmo de ordenação eficiente que utiliza a estratégia "dividir para conquistar" para ordenar uma lista de elementos. Ele é conhecido por sua eficiência e estabilidade, tornando-se uma escolha popular em grande parte das aplicações.

#### Funcionamento:

1. **Dividir:**
   O MergeSort começa dividindo a lista original em duas metades aproximadamente iguais. Esse processo é repetido recursivamente até que cada sublista contenha apenas um elemento. Isso é alcançado dividindo a lista pela metade em cada chamada recursiva.

2. **Conquistar:**
   Depois que as sublistas contêm apenas um elemento, elas são consideradas ordenadas por definição.

3. **Combinar:**
   Em seguida, as sublistas ordenadas são juntas para formar sublistas maiores e ordenadas. Esse processo de mesclagem continua recursivamente até que toda a lista original seja reconstruída e ordenada.

#### Complexidade:

O tempo de execução do MergeSort é O(n log n) no pior caso, onde 'n' é o número de elementos na lista. Isso faz com que o MergeSort seja um dos algoritmos de ordenação mais eficientes em de tempo. Além disso, o MergeSort possui uma complexidade de espaço de O(n), pois requer espaço adicional para armazenar as sublistas durante a mesclagem.

#### Algoritmo:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Dividindo a lista em duas partes
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Realizando ordenacao das metades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    # Realizando comparacao
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Elementos restantes sendo adicionados
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result

# Exemplo de uss
arr = [3, 7, 2, 1, 6, 4, 5]
sorted_arr = merge_sort(arr)
print(sorted_arr)
```

## [QuickSort](#quicksort)

O QuickSort é um dos algoritmos de ordenação mais rápidos e eficientes. 

#### Funcionamento:

1. **Escolha do Pivô:**
   O QuickSort seleciona um elemento da lista como pivô. O pivô pode ser escolhido de várias maneiras, mas comumente é o último elemento da lista.

2. **Particionamento:**
   O QuickSort arruma os elementos da lista de forma que todos os elementos menores que o pivô fiquem antes dele e todos os elementos maiores fiquem depois. Após esse processo, o pivô está na sua posição final na lista ordenada. Isso é feito de maneira eficiente usando duas variáveis, uma que percorre a lista da esquerda para a direita e outra da direita para a esquerda, trocando elementos quando necessário até que os índices se cruzem.

3. **Recursão:**
   Após o passo de partição, o QuickSort é aplicado recursivamente às duas metades resultantes (à esquerda e à direita do pivô), até que toda a lista esteja ordenada.

#### Complexidade:

O tempo de execução do QuickSort é O(n log n) no caso médio e O(n^2) no pior caso. No entanto, na prática, o QuickSort é muito eficiente e geralmente supera outros algoritmos de ordenação, como o MergeSort e o HeapSort, principalmente devido à sua implementação eficiente e baixo uso de memória.

#### Algoritmo:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Realizando escolha do pivo
    left = [x for

 x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Exemplo de uso
arr = [3, 7, 2, 1, 6, 4, 5]
sorted_arr = quick_sort(arr)
print(sorted_arr)
```

## [Selection Sort](#selection-sort)

O Selection Sort é um algoritmo simples de ordenação que divide a lista em duas partes: uma parte ordenada e outra não ordenada. Ele seleciona repetidamente o menor (ou maior, dependendo da ordem desejada) elemento da parte não ordenada e o coloca no final da parte ordenada.

#### Funcionamento:

1. **Encontrar o Menor Elemento:**
   O Selection Sort encontra o menor elemento na parte não ordenada da lista.

2. **Troca:**
   Ele troca o menor elemento encontrado com o primeiro elemento da parte não ordenada, colocando-o no final da parte ordenada.

3. **Repetição:**
   Esse processo é repetido para os elementos restantes da parte não ordenada até que toda a lista esteja ordenada.

#### Complexidade:

O tempo de execução do Selection Sort é O(n^2) no pior caso, onde 'n' é o número de elementos na lista. Apesar de sua simplicidade, o Selection Sort não é eficiente para grandes conjuntos de dados devido ao seu alto número de comparações e trocas.

#### Algoritmo:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Realizando  troca do elemento baixo com o primeiro elemento nao ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Exemplo de uso
arr = [3, 7, 2, 1, 6, 4, 5]
sorted_arr = selection_sort(arr)
print(sorted_arr)
```

## [Insertion Sort](#insertion-sort)

O Insertion Sort é um algoritmo de ordenação siimples que percorre a lista da esquerda para a direita, inserindo cada elemento na posição correta na parte ordenada da lista.

#### Funcionamento:

1. **Parte Ordenada e Não Ordenada:**
   O Insertion Sort divide a lista em duas partes: uma parte ordenada e outra não ordenada. Inicialmente, a parte ordenada contém apenas o primeiro elemento da lista, e a parte não ordenada contém os elementos restantes.

2. **Inserção:**
   O algoritmo percorre a parte não ordenada da lista. Para cada elemento, ele o compara com os elementos na parte ordenada e o insere na posição correta na parte ordenada, deslocando os elementos maiores conforme necessário.

3. **Repetição:**
   Esse processo é repetido até que toda a lista esteja ordenada.

#### Complexidade:

O tempo de execução do Insertion Sort é O(n^2) no pior caso, onde 'n' é o número de elementos na lista. Apesar de sua simplicidade, o Insertion Sort é eficiente para listas pequenas ou quase ordenadas.

#### Algoritmo:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move os elementos maiores para a direita
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Exemplo de uso
arr = [3, 7, 2, 1, 6, 4, 5]
sorted_arr = insertion_sort(arr)
print(sorted_arr)
```

## Exemplo de uso MergeSort

O exemplo abaixo esta simulando um sistema para classificar times de futebol com base em sua pontuação na temporada, informando o time campeão. 

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx]['pontuacao'] > right[right_idx]['pontuacao']:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result

def main():
    times = []
    
    # Capturando os dados dos times
    print("Digite o nome de cada time e sua pontuação (ou deixe em branco para parar):")
    while True:
        nome = input("Nome do time: ")
        if not nome:
            break
        pontuacao = int(input("Pontuação do time: "))
        times.append({'nome': nome, 'pontuacao': pontuacao})
    
    print("\nLista de times (desordenada):")
    for time in times:
        print(f"{time['nome']} - {time['pontuacao']} pontos")
    
    # Ordenando a lista de times com base nas pontuações utilizando o Merge Sort
    times_ordenados = merge_sort(times)
    
    print("\nLista de times (ordenada por pontuação, decrescente):")
    for i, time in enumerate(times_ordenados, start=1):
        print(f"{i}. {time['nome']} - {time['pontuacao']} pontos")
    
    # Identificando o campeão (time com maior pontuação)
    if times_ordenados:
        campeao = times_ordenados[0]['nome']
        pontuacao_campeao = times_ordenados[0]['pontuacao']
        print(f"\nO campeão é: {campeao} com {pontuacao_campeao} pontos!")
    else:
        print("\nNão há times na lista!")

if __name__ == "__main__":
    main()
```

## Exemplo de uso QuickSort

O exemplo abaixo é um gerenciamento de estoque para uma loja, onde é preciso ordenar os produtos com base em diferentes critérios, como preço, quantidade em estoque ou popularidade de venda.

```python
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
```
