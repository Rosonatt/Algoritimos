entregas = []

def cadastrar_entrega(codigo, fornecedor, cliente, endereco, status):
    entrega = {
        "codigo" : codigo,
        "fornecedor": fornecedor,
        "cliente":cliente,
        "destino": endereco,
        "status" : status
    }

    entregas.append(entrega)
    print(f"A entrega {codigo} foi cadastrada com sucesso!")


def buscar_entrega(codigo:str):
    for entrega in entregas:
        if entrega["codigo"] == codigo:
            return print(f"Código: {entrega["codigo"]}, Fornecedor: {entrega["fornecedor"]}, Cliente: {entrega["cliente"]}, Destino: {entrega["destino"]}, Status: {entrega["status"]}")
        
    else:
            print("Desculpe a entrega não foi encontrada.")

def atualizar_status(codigo:str, n_status):
    for entrega in entregas:
        if entrega["codigo"] == codigo:
            entrega["status"] = n_status
            print(f"O Status da entrega {codigo} foi atualizado com sucesso pra {n_status}")
            return
        
    else: 
        print(f" Desculpe o código {codigo} não foi encontrado")
        
  
                 
def listar_entregas():
    if entregas is not None:
        for entrega in entregas:
            print(f"Código: {entrega["codigo"]}, Fornecedor: {entrega["fornecedor"]}, Cliente: {entrega["cliente"]}, Destino: {entrega["destino"]}, Status: {entrega["status"]}")
            return
    print("Não há entregas disponíveis no momento.")

def contar_entregas_por_fornecedor(fornecedor):
    contar = 0
    for entrega in entregas:
        if entrega["fornecedor"] == fornecedor:
            contar += 1

    print(f"A quantidade de entregas do {fornecedor} é {contar}")

cadastrar_entrega("E001", "Fornecedor A", "Cliente X", "Rua 1, Cidade A", "Pendente")  
cadastrar_entrega("E002", "Fornecedor B", "Cliente Y", "Rua 2, Cidade B", "Em Transporte")  
cadastrar_entrega("E003", "Fornecedor A", "Cliente Z", "Rua 3, Cidade C", "Entregue")

listar_entregas()

buscar_entrega("E001")
buscar_entrega("E004")

atualizar_status("E001","Em transporte")
atualizar_status("E004","Em transporte")
contar_entregas_por_fornecedor("Fornecedor A")
contar_entregas_por_fornecedor("Fornecedor B")
contar_entregas_por_fornecedor("Fornecedor C")