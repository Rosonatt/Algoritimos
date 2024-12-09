from datetime import datetime
import os

def registrar_evento():
    try:
        descricao = input("Digite a descrição do evento: ")
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open("sistema_log.txt", "a") as arquivo:
            arquivo.write(f"{data_hora} - Evento: {descricao}\n")
            
        print("Evento registrado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao registrar evento: {str(e)}")

def visualizar_log():
    try:
        if not os.path.exists("sistema_log.txt"):
            print("Arquivo de log ainda não existe.")
            return
            
        with open("sistema_log.txt", "r") as arquivo:
            conteudo = arquivo.read()
            
        if not conteudo:
            print("O arquivo de log está vazio.")
        else:
            print("\n=== HISTÓRICO DE EVENTOS ===")
            print(conteudo)
            
    except Exception as e:
        print(f"Erro ao ler arquivo de log: {str(e)}")

while True:
    print("\n1 - Registrar novo evento")
    print("2 - Visualizar log") 
    print("3 - Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        registrar_evento()
    elif opcao == "2":
        visualizar_log()
    elif opcao == "3":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!")