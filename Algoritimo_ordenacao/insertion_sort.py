def insertion_sort(lista):
    """
    Ordena uma lista de números usando o algoritmo Insertion Sort.

    Parâmetros:
    lista (list): Lista de números a ser ordenada.

    Retorna:
    list: Lista ordenada.
    """
    
    n = len(lista)  # Determina o tamanho da lista.

    # Itera através de cada elemento da lista, começando pelo segundo.
    for i in range(1, n):
        # O elemento atual a ser inserido na posição correta.
        elemento = lista[i]
        j = i - 1  # Índice do elemento anterior.

        # Move os elementos maiores que `elemento` uma posição para frente.
        while j >= 0 and lista[j] > elemento:
            lista[j + 1] = lista[j]  # Move o elemento para frente.
            j -= 1  # Passa para o próximo elemento à esquerda.

        # Insere o elemento na posição correta.
        lista[j + 1] = elemento

    return lista  # Retorna a lista ordenada.


# Exemplo de uso do Insertion Sort
lista = [29, 10, 14, 37, 13]
lista_ordenada = insertion_sort(lista)

# Imprime o resultado
print(f"Lista original: {lista}")
print(f"Lista ordenada: {lista_ordenada}")

