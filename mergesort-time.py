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
