clientes = []

def adicionar(nome, email, telefone, endereco):
    cliente_dados = [nome, email, telefone, endereco]
    clientes.append(cliente_dados)

def exibir_clientes():
    if not clientes:
        print(f"Nenhum cliente cadastrado.")
    else:
        for i, cliente in enumerate(clientes, start=1):
            print(f"Cliente {i}:")
            print(f"Nome: {cliente[0]}")
            print(f"Email: {cliente[1]}")
            print(f"Telefone: {cliente[2]}")
            print(f"Endereço: {cliente[3]}")
            print()  

def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"Cliente encontrado:")
            print(f"  Nome: {cliente[0]}")
            print(f"  Email: {cliente[1]}")
            print(f"  Telefone: {cliente[2]}")
            print(f"  Endereço: {cliente[3]}")
            return
    print("Cliente não encontrado.")

def remover_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            clientes.remove(cliente)
            print(f"Cliente com e-mail {email} foi removido.")
            return
    print(f"Cliente não encontrado.")

def menu():
    print("\nMenu de opções:")
    print(f"1. Adicione clientes")
    print(f"2. Exibir clientes registrados")
    print(f"3. Buscando clientes regisdtrados pelo email")
    print(f"4. Removendo cliente clientes registrados por email")
    print(f"5. Sair do sitemsa")

while True:
    menu()
    escolhas_menu = input(f"Escolha uma opção: ")

    if escolhas_menu == '1':
        
        dig_nome = input(f"Digite o seu nome: ")
        dig_email = input(f"Digite o seu email: ")
        dig_telefone = input(f"Digite o seu telefone: ")
        dig_endereco = input(f"Digite o seu endereço: ")

        nome_str = str(dig_nome)
        email_str = str(dig_email)
        telefone_str = str(dig_telefone)
        endereco_str = str(dig_endereco)


        adicionar(dig_nome, dig_email, dig_telefone, dig_endereco)
        print("Cliente foi adicionado !")
        
    elif escolhas_menu == '2':
        
        exibir_clientes()
        
    elif escolhas_menu == '3':
        
        buscando_email = input(f"Digite o e-mail do cliente que deseja obter as informações: ")
        buscar_cliente(buscando_email)
        
    elif escolhas_menu == '4':
        
        removendo_email = input(f"Digite o e-mail do cliente que deseja remover da lista: ")
        remover_cliente(removendo_email)
        
    elif escolhas_menu == '5':
        
        print(f"Saindo do sistema")
        break
        
    else:
        print(f"Opção inválida! Tente novamente.")




        
        



