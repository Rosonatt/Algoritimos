lista_de_tarefas = []
proximo_id = 1  

def criar_id_unico():
    global proximo_id
    new_id = proximo_id
    proximo_id += 1
    return new_id

def adc_tarefa(descricao, status, prioridade):
    new_id = criar_id_unico()
    tarefa_n = {
        'Id': new_id,
        'Descrição': descricao,
        'Status': status,
        'Prioridade': prioridade
    }
    lista_de_tarefas.append(tarefa_n)

def visu_tarefas(tarefas=None):
    if tarefas is None:
        tarefas = lista_de_tarefas
    
    if not tarefas:
        print("Nenhuma tarefa a ser exibida.")
        return
    
    print(f"{'ID':<5} {'Descrição':<30} {'Status':<15} {'Prioridade':<10}")
    print("-" * 60)
    for tarefa in tarefas:
        print(f"{tarefa['id']:<5} {tarefa['descricao']:<30} {tarefa['status']:<15} {tarefa['prioridade']:<10}")

def filtrando_tarefa(status=None, prioridade=None):
    tarefas_filtradas = lista_de_tarefas
    if status:
        tarefas_filtradas = [tarefa for tarefa in tarefas_filtradas if tarefa['status'] == status]
    if prioridade:
        tarefas_filtradas = [tarefa for tarefa in tarefas_filtradas if tarefa['prioridade'] == prioridade]
    return tarefas_filtradas

def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        limpar_tela()
        print("==== Gerenciador de Tarefas ====")
        print("1 - Adicionar uma tarefa")
        print("2 - Visualizar Todas as Tarefas")
        print("3 - Filtrar Tarefas")
        print("4 - Sair do sistema")
        print("===============================")
        
        escolha = input("Escolha uma opção (1-4): ")
        
        if escolha == "1":
            descricao = input("Descrição da tarefa: ")
            status = input("Status da tarefa (pendente, em andamento, concluida): ")
            prioridade = input("Prioridade da tarefa (alta, media, baixa): ")
            adc_tarefa(descricao, status, prioridade)
            print("Tarefa adicionada com sucesso!")
        
        elif escolha == "2":
            visu_tarefas()
            input("Pressione Enter para voltar ao menu.")
        
        elif escolha == "3":
            status = input("Filtrar por status (ou deixe em branco para todos): ")
            prioridade = input("Filtrar por prioridade (ou deixe em branco para todos): ")
            tarefas_filtradas = filtrando_tarefa(status=status if status else None, prioridade=prioridade if prioridade else None)
            if tarefas_filtradas:
                visu_tarefas(tarefas_filtradas)
            else:
                print("Nenhuma tarefa atende aos filtros aplicados.")
            input("Pressione Enter para voltar ao menu.")
        
        elif escolha == "4":
            print("Saindo do sistema. Até mais!")
            break
        
        else:
            print("Essa opção é inválida. Tente novamente.")
            input("Pressione Enter para voltar ao menu.")

menu()
