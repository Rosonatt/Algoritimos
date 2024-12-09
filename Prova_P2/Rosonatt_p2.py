documentos = []
autores = []
areas = []
emprestimos = []

def adc_documentos():
    documento = {}
    documento["titulo"] = input("Digite título do documento: ")
    documento["data_producao"] = input("Data de produção: ")
    documento["tema"] = input("Tema: ")
    documento["contexto"] = input("Contexto: ")
    documento["descricao"] = input("Descrição: ")
    documento["autor"] = input("Autor: ")
    documento["localizacao"] = input("Localização na biblioteca: ")

    documentos.append(documento)
    print(f"Parabéns documento foi adicionado com sucesso !!.")

def adc_autor():
    nome = input(f"Digite  nome do autor: ")
    data_de_nascimento = input(f"Digite a data de nascimento: ")
    local_de_nascimento = input(f" Digite local de nascimento: ")
    biografia = input(f"Qual biografia: ")
    areas_pesquisadas_pelo_autor = input(f"Áreas de pesquisa (separe todas  por vírgula): ").split(',')
    autores.append({"nome": nome, "data_nascimento": data_de_nascimento, "local_nascimento": local_de_nascimento, "biografia": biografia, "areas_pesquisa": [area.strip() for area in areas_pesquisadas_pelo_autor]})
    print("Autor foi  adicionado com sucesso!!!.")

def adc_area():
    titulo = input(f"Adicione  um titulo : ")
    periodo = input(f"qual o período de estudo?: ")
    descricao = input(f" Digite uma descrição: ")
    obras = input(f"quais obras represent(separe cada um po por vírgula): ").split(',')
    areas.append({"Titulo": titulo, "periodo_estudo": periodo, "descricao": descricao, "obras_representativas": [obra.strip() for obra in obras]})
    print("Área de pesquisa adicionada com sucesso.")

def emprestimo_de_documentos():
    documento = input(f"Digite o título do documento emprestado: ")
    periodo_emprestimo = input(f"Período de empréstimo: ")
    nome_evento = input(f"Nome do evento: ")
    responsavel = input(f"Responsável: ")
    tema = input(f"Tema do evento: ")
    emprestimos.append({"documento": documento, "periodo_emprestimo": periodo_emprestimo, "nome_evento": nome_evento, "responsavel": responsavel, "tema": tema})
    print(f"Empréstimo foi registrado com sucesso.")

def salvar_dados(arquivo):
    try:
        with open(arquivo, 'w') as f:
            for doc in documentos:
                f.write(str(doc) + '\n')
            for autor in autores:
                f.write(str(autor) + '\n')
            for area in areas:
                f.write(str(area) + '\n')
            for emprestimo in emprestimos:
                f.write(str(emprestimo) + '\n')
        print(f"Dados salvos com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados: {e}")

def carregar_dados(arquivo):
    global documentos, autores, areas, emprestimos
    try:
        with open(arquivo, 'r') as f:
            for line in f:
                if line.strip():
                    documentos.append(eval(line.strip()))
        print("Dados carregados com sucesso!!!.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]["titulo"]
    left = [x for x in array if x["titulo"] < pivot]
    middle = [x for x in array if x["titulo"] == pivot]
    right = [x for x in array if x["titulo"] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def menu():
    while True:
        print("\nMenu:")
        print(f"1. Adicionar Documento")
        print(f"2. Adicionar Autor")
        print(f"3. Adicionar Área de Pesquisa")
        print(f"4. Registrar Empréstimo")
        print(f"5. Salvar Dados")
        print(f"6. Carregar Dados")
        print(f"7. Listar Documentos")
        print(f"8. Sair")
        opcao = input(f"Escolha uma  das opções: ")
        if opcao == '1':
            adc_documentos()
        elif opcao == '2':
            adc_autor()
        elif opcao == '3':
            adc_area()
        elif opcao == '4':
            emprestimo_de_documentos()
        elif opcao == '5':
            salvar_dados("salvar_dados.txt")
        elif opcao == '6':
            carregar_dados("salvar_dados.txt")
        elif opcao == '7':
            documentos_ordenados = quick_sort(documentos)
            for doc in documentos_ordenados:
                print(doc)
        elif opcao == '8':
            print(f"Saindo...")
            break
        else:
            print(f"Opção inválida. Por favor  tente novamente!!.")

menu()