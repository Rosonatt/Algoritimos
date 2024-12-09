def quick_sort(arr):
    """
    Ordena uma lista de números usando o algoritmo Quick Sort.

    Parâmetros:
    arr (list): Lista de números a ser ordenada.

    Retorna:
    list: Lista ordenada.
    """
    # Caso base: Se a lista tem 0 ou 1 elemento, já está ordenada.
    if len(arr) <= 1:
        return arr
    
    # Escolhendo o pivô (último elemento da lista).
    pivo = arr[-1]

    # Dividindo a lista em três partes:
    # 1. Elementos menores que o pivô.
    esquerda = [x for x in arr[:-1] if x < pivo]

    # 2. Elementos iguais ao pivô.
    iguais = [x for x in arr if x == pivo]

    # 3. Elementos maiores que o pivô.
    direita = [x for x in arr[:-1] if x > pivo]

    # Chamando recursivamente o Quick Sort para as sublistas e combinando os resultados.
    return quick_sort(esquerda) + iguais + quick_sort(direita)


# Exemplo de uso
lista = [10, 25, 72, 11, 8, 9, 14, 12, 31, 16]
lista_ordenada = quick_sort(lista)

# Imprimindo os resultados
print(f"Lista original: {lista}")
print(f"Lista ordenada: {lista_ordenada}")

