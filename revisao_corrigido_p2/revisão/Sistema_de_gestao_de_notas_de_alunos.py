import os

def carregar_dados(arquivo):
    alunos = []
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                nome, media = linha.strip().split(', ')
                alunos.append({'nome': nome, 'media': float(media)})
    except FileNotFoundError:
        pass  
    return alunos

def salvar_dados(arquivo, alunos):
    try:
        with open(arquivo, 'w') as f:
            for aluno in alunos:
                f.write(f"{aluno['nome']}, {aluno['media']:.2f}\n")
    except (IOError, OSError) as e:
        print(f"Erro ao salvar os dados no arquivo: {e}")

def solicitar_dados_aluno():
    nome = input("Digite o nome do aluno: ")
    notas = []

    while len(notas) < 2 or len(notas) > 5:
        notas_input = input("Digite as notas do aluno (separadas por espaço, mínimo 2 e máximo 5): ").split()
        notas = []
        for nota in notas_input:
            try:
                nota_float = float(nota)
                if 0 <= nota_float <= 10:
                    notas.append(nota_float)
                else:
                    raise ValueError("Nota inválida. Deve ser entre 0 e 10.")
            except ValueError as ve:
                print(f"Erro: {ve}. Tente novamente.")
                notas = []  
                break  

        if len(notas) < 2 or len(notas) > 5:
            print("Erro: Você deve inserir entre 2 e 5 notas.")

    media = sum(notas) / len(notas)
    return {'nome': nome, 'notas': notas, 'media': media}

def adicionar_aluno(alunos):
    novo_aluno = solicitar_dados_aluno()
    alunos.append(novo_aluno)
    salvar_dados('alunos.txt', alunos)
    print(f'Aluno {novo_aluno["nome"]} adicionado com sucesso. Média: {novo_aluno["media"]:.2f}')

def ordenar_alunos(alunos):
    alunos.sort(key=lambda aluno: aluno['media'], reverse=True)
    print("Alunos ordenados por média:")
    for aluno in alunos:
        print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")

def salvar_em_arquivo(alunos, nome_arquivo='alunos.txt'):
    if os.path.exists(nome_arquivo):
        resposta = input(f"O arquivo '{nome_arquivo}' já existe. Deseja sobrescrevê-lo? (s/n): ").strip().lower()
        if resposta != 's':
            print("Operação cancelada. Os dados não foram salvos.")
            return

    salvar_dados(nome_arquivo, alunos)

arquivo_txt = 'alunos.txt'
alunos = carregar_dados(arquivo_txt)

while True:
    opcao = input("Deseja adicionar um aluno? (s/n): ").strip().lower()
    if opcao == 's':
        adicionar_aluno(alunos) 
    else:
        break  

ordenar_alunos(alunos)    
salvar_em_arquivo(alunos) 