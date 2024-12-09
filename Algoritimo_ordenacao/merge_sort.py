def merge_sort(lista):
    """
    Ordena uma lista de números usando o algoritmo Merge Sort.

    Parâmetros:
    lista (list): Lista de números a ser ordenada.

    Retorna:
    list: Lista ordenada.
    """

    # Caso base: Se a lista tem 0 ou 1 elemento, já está ordenada.
    if len(lista) <= 1:
        return lista

    # Dividindo a lista ao meio.
    mid = len(lista) // 2
    metade_esquerda = merge_sort(lista[:mid])  # Ordena a metade esquerda.
    metade_direita = merge_sort(lista[mid:])   # Ordena a metade direita.

    # Junta as duas metades ordenadas.
    return merge(metade_esquerda, metade_direita)


def merge(esquerda, direita):
    """
    Combina duas sublistas ordenadas em uma única lista ordenada.

    Parâmetros:
    esquerda (list): Primeira sublista ordenada.
    direita (list): Segunda sublista ordenada.

    Retorna:
    list: Lista ordenada contendo todos os elementos das sublistas.
    """
    lista_ordenada = []  # Lista para armazenar os elementos ordenados.
    i = 0  # Índice para a sublista esquerda.
    j = 0  # Índice para a sublista direita.

    # Compara os elementos de ambas as sublistas e adiciona o menor à lista ordenada.
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            lista_ordenada.append(esquerda[i])
            i += 1
        else:
            lista_ordenada.append(direita[j])
            j += 1

    # Adiciona os elementos restantes da sublista esquerda (se houver).
    lista_ordenada.extend(esquerda[i:])

    # Adiciona os elementos restantes da sublista direita (se houver).
    lista_ordenada.extend(direita[j:])

    return lista_ordenada


# Exemplo de uso do Merge Sort
lista = [10, 25, 72, 11, 8, 9, 14, 12, 31, 16]
lista_ordenada = merge_sort(lista)

# Imprime o resultado
print(f"Lista original: {lista}")
print(f"Lista ordenada: {lista_ordenada}")

