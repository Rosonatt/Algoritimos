from insertion_sort import insertion_sort

def bucket_sort(lista):
    """
    Ordena uma lista de números no intervalo [0, 1) usando o algoritmo Bucket Sort.

    Parâmetros:
    lista (list): Uma lista de números reais entre 0 e 1.

    Retorna:
    list: Lista ordenada.
    """

    # Passo 1: Determinar o número de buckets com base no tamanho da lista
    n = len(lista)
    # Cria uma lista de buckets vazios
    buckets = [[] for _ in range(n)]

    # Passo 2: Distribuir os elementos entre os buckets
    for num in lista:
        # Calcula o índice do bucket para cada número (baseado em n * valor do número)
        index = int(num * n)
        buckets[index].append(num)  # Adiciona o número no bucket correspondente

    # Passo 3: Ordenar cada bucket individualmente
    for bucket in buckets:
        # Usamos o Insertion Sort para ordenar os elementos de cada bucket
        insertion_sort(bucket)

    # Passo 4: Concatenar os buckets ordenados em uma única lista
    lista_ordenada = []  # Lista que armazenará o resultado final
    for bucket in buckets:
        lista_ordenada.extend(bucket)  # Adiciona os elementos do bucket à lista final

    return lista_ordenada  # Retorna a lista ordenada

# Exemplo de uso do algoritmo:
lista = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
lista_ordenada = bucket_sort(lista)

# Imprime os resultados
print(f"Lista original: {lista}")
print(f"Lista ordenada: {lista_ordenada}")
