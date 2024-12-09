"""
Heap Sort:
Esse algoritmo transforma a lista em uma estrutura de heap, onde o maior elemento sempre fica 
no topo e então realiza a ordenação removendo o maior elemento (para Max-Heap) e 
reorganizando o restante para manter a propriedade do heap.

Vantagens:
    Uso Eficiente de Memória;
    Estável em termos de desempenho para todos os casos e distribuições de dados, diferentemente do QuickSort;
    

Desvantagens:
    Algoritmo um pouco mais complexo de entender e não é amigavél para iniciantes;

Passo a Passo:
    Converte A lista é convertida em um Max-Heap, onde cada nó é maior ou igual a seus filhos.
    Defini o maior ou o menor elemento como raiz.
    Coloca os elementos do Heap no final da lista de forma ordenada.
"""
def heapify(lista, n, i):
    
    maior = i # Inicioando o nó atual como o maior.
    esquerda = 2 * i + 1 # Índice do filho da esquerda
    direita = 2 * i + 2 # Índice do filho da direita
    
    # Se o filho à esquerda existir e for maior que o nó atual
    if esquerda < n and lista[i] < lista[esquerda]:
        maior = esquerda

    #Se o filho à direita existe e for maior que o maior encontrado até agora
    if direita < n and lista[maior] < lista[direita]:
        maior = direita

    # Se o maior não é o nó atual, ele troca e continua 
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)
    
    return lista

def heap_sort(lista):
    
    n = len(lista)

    # Construindo o Max-Heap
    for i in range(n // 2, -1, -1):
        heapify(lista, n, i)

    # Extraindo os elementos do heap
    for i in range(n - 1, 0, -1):

        # Movendo a raiz atual para o final
        lista[i], lista[0] = lista[0], lista[i]
        # Chamando o heapify para o heap reduzido
        heapify(lista, i, 0)
    
    return lista

# Exemplo

lista = [10, 25, 72, 11, 8, 9, 14, 12, 31, 16]
heap_sort(lista)
print(f'\nLista ordenada: {lista}\n')