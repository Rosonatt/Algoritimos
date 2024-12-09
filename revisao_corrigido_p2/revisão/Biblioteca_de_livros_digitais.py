import os

livros = []

def adicionar_livro():
    try:
        titulo = input("Título do livro: ")
        autor = input("Autor: ")
        
        while True:
            ano = input("Ano de publicação: ")
            if ano.isdigit() and int(ano) > 0:
                ano = int(ano)
                break
            else:
                print("Por favor, insira um ano válido (número positivo).")
        
        
        while True:
            paginas = input("Número de páginas: ")
            if paginas.isdigit() and int(paginas) > 0:
                paginas = int(paginas)
                break
            else:
                print("Por favor, insira um número de páginas válido (número positivo).")
        
        livro = {'titulo': titulo, 'autor': autor, 'ano': ano, 'paginas': paginas}
        livros.append(livro)
        print("Livro adicionado com sucesso!")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Páginas: {livro['paginas']}")

def ordenar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    
    criterio = input("Ordenar por (1) Ano ou (2) Páginas? ")
    ordem = input("Ordenar em (C)rescente ou (D)ecrescente? ").upper()
    
    if criterio == '1':
        livros.sort(key=lambda x: x['ano'], reverse=(ordem == 'D'))
    elif criterio == '2':
        livros.sort(key=lambda x: x['paginas'], reverse=(ordem == 'D'))
    else:
        print("Critério inválido.")
        return

    print("Livros ordenados com sucesso!")

def salvar_livros():
    try:
        with open('biblioteca.txt', 'w') as f:
            for livro in livros:
                linha = f"{livro['titulo']},{livro['autor']},{livro['ano']},{livro['paginas']}\n"
                f.write(linha)
        print("Os dados foram salvos no arquivo 'biblioteca.txt'.")
    except IOError as e:
        print(f"Ocorreu um erro ao salvar os dados: {e}")

def carregar_livros():
    if not os.path.exists('biblioteca.txt'):
        print("Arquivo 'biblioteca.txt' não encontrado.")
        return
    
    try:
        with open('biblioteca.txt', 'r') as f:
            for linha in f:
                titulo, autor, ano, paginas = linha.strip().split(',')
                livro = {
                    'titulo': titulo,
                    'autor': autor,
                    'ano': int(ano),
                    'paginas': int(paginas)
                }
                livros.append(livro)
        print("Livros carregados com sucesso!")
    except IOError as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")
    except ValueError:
        print("Erro nos dados do arquivo. Verifique o formato.")

while True:
    print("\nBem-vindo à Biblioteca Digital!")
    print("Escolha uma opção:")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Ordenar livros")
    print("4. Salvar dados em arquivo")
    print("5. Carregar dados do arquivo")
    print("6. Sair")
    
    opcao = input("> ")
    
    if opcao == '1':
        adicionar_livro()
    elif opcao == '2':
        listar_livros()
    elif opcao == '3':
        ordenar_livros()
    elif opcao == '4':
        salvar_livros()
    elif opcao == '5':
        carregar_livros()
    elif opcao == '6':
        if input("Deseja salvar os dados antes de sair? (S/N): ").upper() == 'S':
            salvar_livros()
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")