def counting_sort(lista):
    """
    Ordena uma lista de números inteiros usando o algoritmo Counting Sort.

    Parâmetros:
    lista (list): Lista de números inteiros a ser ordenada.

    Retorna:
    list: Lista ordenada.
    """

    # Passo 1: Encontrar o valor máximo na lista para determinar o intervalo dos dados.
    valor_max = max(lista)  # O maior número define o tamanho da lista de contagem.

    # Passo 2: Criar a lista de contagem, inicializando com zeros.
    # O tamanho da lista é o maior número mais 1, para acomodar todos os índices.
    count = [0] * (valor_max + 1)

    # Passo 3: Contar a frequência de cada número na lista original.
    # Cada índice da lista `count` armazenará quantas vezes o número correspondente aparece.
    for num in lista:
        count[num] += 1

    # Passo 4: Atualizar a lista de contagem para armazenar as posições cumulativas.
    # Isso ajudará a determinar a posição final de cada número na lista ordenada.
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Passo 5: Criar uma lista auxiliar para armazenar a lista ordenada.
    # O tamanho dessa lista é igual ao tamanho da lista original.
    output = [0] * len(lista)

    # Passo 6: Preencher a lista ordenada processando os elementos da lista original de trás para frente.
    # Isso garante que o algoritmo seja estável (mantém a ordem relativa de elementos iguais).
    for num in reversed(lista):
        index = count[num] - 1  # Determina a posição correta do número na lista ordenada.
        output[index] = num  # Coloca o número na posição correta.
        count[num] -= 1  # Decrementa o contador para lidar com repetições.

    return output  # Retorna a lista ordenada.

# Exemplo de uso do algoritmo Counting Sort
lista = [10, 25, 72, 11, 8, 9, 14, 12, 31, 16]
lista_ordenada = counting_sort(lista)

# Exibe os resultados: lista original e lista ordenada.
print(f"Lista original: {lista}")
print(f"Lista ordenada: {lista_ordenada}")


