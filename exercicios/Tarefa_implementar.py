'''Tarefa de Implementação 
Descrição do Sistema
O sistema de gerenciamento de estoque de livros permite que a biblioteca cadastre, atualize, 
remova, e busque livros, bem como verifique a quantidade de exemplares disponíveis de cada 
livro. Os livros serão armazenados em uma lista, onde cada elemento é um dicionário que 
representa um livro com informações como título, autor, gênero, quantidade em estoque e 
código do livro. O sistema usará diversas funções para manipular a lista de dicionários.
Atores
• Bibliotecário: Responsável por gerenciar o estoque de livros.
Fluxo Principal de Casos de Uso
1. Cadastrar Livro
o O bibliotecário pode cadastrar um novo livro no sistema, informando o título, 
autor, gênero, quantidade e código do livro.
o O sistema armazena esses dados em um dicionário e adiciona o dicionário à lista 
de livros.
2. Buscar Livro por Código
o O bibliotecário pode buscar um livro pelo seu código.
o O sistema percorre a lista de livros para encontrar o dicionário que contém o 
código informado e retorna os detalhes do livro. Se o livro não for encontrado, 
uma mensagem de erro é exibida.
3. Atualizar Estoque de um Livro
o O bibliotecário pode atualizar a quantidade de exemplares de um livro 
específico.
o O sistema localiza o livro pelo código e atualiza o valor da chave "quantidade" no 
dicionário correspondente.
4. Remover Livro do Sistema
o O bibliotecário pode remover um livro do estoque, informando o código do livro.
o O sistema procura o livro pelo código e remove o dicionário correspondente da 
lista.
5. Listar Todos os Livros
o O bibliotecário pode solicitar a listagem de todos os livros cadastrados no 
sistema.
o O sistema percorre a lista de livros e exibe as informações de cada dicionário, 
como título, autor, gênero, quantidade e código.
Requisitos Funcionais
1. O sistema deve permitir o cadastro de um livro com título, autor, gênero, quantidade e 
código.
2. O sistema deve permitir a busca de um livro pelo código e retornar suas informações.
3. O sistema deve permitir a atualização do estoque de um livro específico.
4. O sistema deve possibilitar a remoção de um livro através de seu código.
5. O sistema deve listar todos os livros cadastrados no sistema.
Requisitos Não Funcionais
1. O sistema deve ser simples e de fácil uso para o bibliotecário.
2. O sistema deve processar as operações de cadastro, busca, atualização, remoção e 
listagem em menos de 2 segundos.
3. Mensagens de erro devem ser exibidas caso o livro não seja encontrado ou os dados 
inseridos estejam incorretos'''

livros_em_estoque = []

def cadas_livros(titulo: str, autor: str, genero: str, quantidade: int, codigo: str):
    livros = {
        "Título": titulo,
        "Autor": autor,
        "Gênero": genero,
        "Quantidade": quantidade,
        "Código": codigo
    }

    livros_em_estoque.append(livros)

    print(f"O livro '{titulo}' foi adicionado ao sistema com êxito!")

def buscando_livros(codigo: str):
    for livro in livros_em_estoque:
        if livro["Código"] == codigo:
            return livro
            
    return None

def estoque_atualizado(codigo, nova_quantidade):
    livro = buscando_livros(codigo)
    if livro:
        livro["Quantidade"] = nova_quantidade
        print(f"A quantidade do livro '{livro['Título']}' foi alterada para {nova_quantidade} unidades.")
    
    else:
        print("Erro: Livro não encontrado.")

def livro_removido(codigo):
    livro = buscando_livros(codigo)
    if livro:
        livros_em_estoque.remove(livro)
        print(f"O livro '{livro['Título']}' foi retirado com sucesso!")
    
    else:
        print("Erro: Livro não encontrado.")

def todos_os_livros():
    if not livros_em_estoque:
        print("Não há livros cadastrados.")
    
    else:
        print("Livros registrados:")
        for livro in livros_em_estoque:
            print(f"Título: {livro['Título']}, Autor: {livro['Autor']}, Gênero: {livro['Gênero']}, "
                  f"Quantidade: {livro['Quantidade']}, Código: {livro['Código']}")

def biblioteca():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Livro")
        print("2. Buscar Livro por Código")
        print("3. Atualizar Estoque de um Livro")
        print("4. Remover Livro do Sistema")
        print("5. Listar Todos os Livros")
        print("6. Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            genero = input("Gênero do livro: ")
            quantidade = int(input("Quantidade em estoque: "))
            codigo = input("Código do livro: ")
            cadas_livros(titulo, autor, genero, quantidade, codigo)

        elif opcao == "2":
            codigo = input("Código do livro que deseja buscar: ")
            livro = buscando_livros(codigo)
            if livro:
                print(f"Livro encontrado: {livro}")
            else:
                print("Erro: Livro não encontrado.")

        elif opcao == "3":
            codigo = input("Código do livro a ser atualizado: ")
            nova_quantidade = int(input("Nova quantidade em estoque: "))
            estoque_atualizado(codigo, nova_quantidade)

        elif opcao == "4":
            codigo = input("Código do livro a ser removido: ")
            livro_removido(codigo)

        elif opcao == "5":
            todos_os_livros()

        elif opcao == "6":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

biblioteca()
