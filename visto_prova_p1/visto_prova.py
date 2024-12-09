'''  que eu corrigi foi o dicionario, eu tinha feito com endereço e quando o senhor pediu prara ser igual ao da prova
  eu renomiei  mas so mudei a string o argumento continuou endereço fiz alteraçao agora toda para endereço mesmo ,apesar de náo 
  mudar a funcionabilidade do codigo eu acho.
  coloquei um print  tbm logo abaixo pra printar as funçoes . mudei a função listar entregas apenas pra  if entregas tbm,  assim ela verifica se a lista esta  vazia
 seguinndo o contexto booleano,  ela teria que me retornar FALSE ja que a lsita não esat vazia, antes ela me reronava TRUE , 
ja que is not None verifica se a variável entregas foi iniciada e não é None. Mesmo que a lista esteja vazia, ainda retornaria True.

acho que é so isso pelo que entendi . coloquei mais um teeste tbm  para   entregas náo encontradas seguindo po padráo de numeros que o senhor pediu na prova.
 tbm e (f'') em alguns prints que estavam sem 
  
'''
entregas = []

def cadastrar_entrega(codigo, fornecedor, cliente, endereco, status):
    entrega = {
        "codigo": codigo,
        "fornecedor": fornecedor,
        "cliente": cliente,
        "endereco": endereco,  
        "status": status
    }
    entregas.append(entrega)
    print(f"A entrega {codigo} foi cadastrada com sucesso!")

def buscar_entrega(codigo: str):
    for entrega in entregas:
        if entrega["codigo"] == codigo:
            return print(f"Código: {entrega['codigo']}, Fornecedor: {entrega['fornecedor']}, Cliente: {entrega['cliente']}, Endereço: {entrega['endereco']}, Status: {entrega['status']}")
    
    print(f"Desculpe, a entrega não foi encontrada.")

def atualizar_status(codigo: str, n_status):
    for entrega in entregas:
        if entrega["codigo"] == codigo:
            entrega["status"] = n_status
            print(f"O Status da entrega {codigo} foi atualizado com sucesso para {n_status}.")
            return
    
    print(f"Desculpe, o código {codigo} não foi encontrado.")

def listar_entregas():
    if entregas:
        for entrega in entregas:
            print(f"Código: {entrega['codigo']}, Fornecedor: {entrega['fornecedor']}, Cliente: {entrega['cliente']}, Endereço: {entrega['endereco']}, Status: {entrega['status']}")
    else:
        print(f"Não há entregas disponíveis no momento.")

def contar_entregas_por_fornecedor(fornecedor):
    contar = 0
    for entrega in entregas:
        if entrega["fornecedor"] == fornecedor:
            contar += 1

    print(f"A quantidade de entregas do {fornecedor} é {contar}.")


cadastrar_entrega("E001", "Fornecedor A", "Cliente X", "Rua 1, Cidade A", "Pendente")  
cadastrar_entrega("E002", "Fornecedor B", "Cliente Y", "Rua 2, Cidade B", "Em Transporte")  
cadastrar_entrega("E003", "Fornecedor A", "Cliente Z", "Rua 3, Cidade C", "Entregue")

print(f"\n todas as entregas:")

listar_entregas()

print(f"\nBuscando todas as entregas:")

buscar_entrega("E001")
buscar_entrega("E004")
buscar_entrega("E005")

print(f"\nAtualizando status de todas as entregas:")

atualizar_status("E001", "Em transporte")
atualizar_status("E004", "Em transporte")
atualizar_status("E005", "Em transporte")

print(f"\nContando entregas por fornecedor:")

contar_entregas_por_fornecedor("Fornecedor A")
contar_entregas_por_fornecedor("Fornecedor B")
contar_entregas_por_fornecedor("Fornecedor C")