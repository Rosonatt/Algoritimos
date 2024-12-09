def radix_sort(lista, base: int = 10):
    """
    Ordena uma lista de números inteiros utilizando o algoritmo Radix Sort.

    Parâmetros:
    lista (list): Lista de números inteiros a ser ordenada.
    base (int): Base do sistema numérico, por padrão é 10 para números decimais.

    Retorna:
    list: Lista ordenada.
    """
    # Passo 1: Inicializa o valor da unidade (exp), que começa com 1 (para as unidades).
    exp = 1

    # Passo 2: Encontrar o valor máximo na lista para determinar até qual dígito devemos ordenar.
    max_valor = max(lista)

    # Passo 3: Repetir o processo de ordenação até que o maior valor não tenha mais dígitos.
    while max_valor // exp > 0:

        # Passo 4: Criar os "buckets" (baldes), onde cada bucket corresponde a um dígito.
        buckets = [[] for _ in range(base)]

        # Passo 5: Distribuir os elementos nos buckets com base no dígito atual.
        for valor in lista:
            index = (valor // exp) % base  # Determina o índice do bucket de acordo com o dígito
            buckets[index].append(valor)

        # Passo 6: Reconstituir a lista a partir dos buckets ordenados.
        lista = [num for bucket in buckets for num in bucket]

        # Passo 7: Avançar para o próximo dígito (dezena, centena, etc.), multiplicando exp por base.
        exp *= base

    # Passo 8: Retornar a lista ordenada.
    return lista


# Exemplo de uso
lista = [10, 25, 72, 11, 8, 9, 14, 12, 31, 16]
lista_ordenada = radix_sort(lista)

# Imprimindo os resultados
print(f"Lista não ordenada: {lista}")
print(f"Lista ordenada: {lista_ordenada}")
