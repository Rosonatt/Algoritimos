import os

estoque = []

def adicionar_produto():
    try:
        nome = input("Nome do produto: ")
        categoria = input("Categoria do produto: ")
        
        while True:
            preco = input("Preço do produto: ")
            try:
                preco = float(preco)
                if preco >= 0:
                    break
                else:
                    print("O preço deve ser um número positivo.")
            except ValueError:
                print("Por favor, insira um preço válido.")
        
        while True:
            quantidade = input("Quantidade do produto: ")
            try:
                quantidade = int(quantidade)
                if quantidade >= 0:
                    break
                else:
                    print("A quantidade deve ser um número inteiro não negativo.")
            except ValueError:
                print("Por favor, insira uma quantidade válida.")

        produto = {'nome': nome, 'categoria': categoria, 'preco': preco, 'quantidade': quantidade}
        estoque.append(produto)
        print("Produto adicionado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def atualizar_quantidade():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    listar_produtos()
    nome_produto = input("Digite o nome do produto que deseja atualizar a quantidade: ")

    for produto in estoque:
        if produto['nome'] == nome_produto:
            while True:
                try:
                    ajuste = int(input("Quantidade a adicionar ou remover (use número negativo para remover): "))
                    produto['quantidade'] += ajuste
                    if produto['quantidade'] < 0:
                        print("A quantidade não pode ser negativa. Ajuste não realizado.")
                        produto['quantidade'] -= ajuste  
                    else:
                        print("Quantidade atualizada com sucesso!")
                    return
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
    
    print("Produto não encontrado.")

def listar_produtos():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    for produto in estoque:
        print(f"Nome: {produto['nome']}, Categoria: {produto['categoria']}, Preço: {produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

def ordenar_produtos():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    
    criterio = input("Ordenar por (1) Preço ou (2) Quantidade? ")
    ordem = input("Ordenar em (C)rescente ou (D)ecrescente? ").upper()
    
    if criterio == '1':
        estoque.sort(key=lambda x: x['preco'], reverse=(ordem == 'D'))
    elif criterio == '2':
        estoque.sort(key=lambda x: x['quantidade'], reverse=(ordem == 'D'))
    else:
        print("Critério inválido.")
        return

    print("Produtos ordenados com sucesso!")

def salvar_estoque():
    try:
        with open('estoque.txt', 'w') as f:
            for produto in estoque:
                linha = f"{produto['nome']},{produto['categoria']},{produto['preco']:.2f},{produto['quantidade']}\n"
                f.write(linha)
        print("Os dados foram salvos no arquivo 'estoque.txt'.")
    except IOError as e:
        print(f"Ocorreu um erro ao salvar os dados: {e}")

def carregar_estoque():
    if not os.path.exists('estoque.txt'):
        print("Arquivo 'estoque.txt' não encontrado.")
        return
    
    try:
        with open('estoque.txt', 'r') as f:
            for linha in f:
                nome, categoria, preco, quantidade = linha.strip().split(',')
                produto = {
                    'nome': nome,
                    'categoria': categoria,
                    'preco': float(preco),
                    'quantidade': int(quantidade)
                }
                estoque.append(produto)
        print("Estoque carregado com sucesso!")
    except IOError as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")
    except ValueError:
        print("Erro nos dados do arquivo. Verifique o formato.")

while True:
    print("\nBem-vindo ao Sistema de Gestão de Estoque!")
    print("Escolha uma opção:")
    print("1. Adicionar produto")
    print("2. Atualizar quantidade")
    print("3. Listar produtos")
    print("4. Ordenar produtos")
    print("5. Salvar estoque")
    print("6. Carregar estoque")
    print("7. Sair")
    
    opcao = input("> ")
    
    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        atualizar_quantidade()
    elif opcao == '3':
        listar_produtos()
    elif opcao == '4':
        ordenar_produtos()
    elif opcao == '5':
        salvar_estoque()
    elif opcao == '6':
        carregar_estoque()
    elif opcao == '7':
        if input("Deseja salvar os dados antes de sair? (S/N): ").upper() == 'S':
            salvar_estoque()
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")