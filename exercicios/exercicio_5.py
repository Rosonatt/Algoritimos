def calcular_media(notas):
   
    if not notas:
        raise ValueError("A lista de notas está vazia.")
   
    return sum(notas) / len(notas)

def exibir_media(notas):
    media = calcular_media(notas)

    if media >= 7:
        print(f"Parabéns! Sua média é {media:.2f} e você foi aprovado.")
    else:
        print(f"Sua média é {media:.2f}. Infelizmente, você não foi aprovado.")

def validar_nota(nota):
    if not 0 <= nota <= 10:
        raise ValueError("A nota deve estar entre 0 e 10.")

try:
    numero_notas = int(input("Quantas notas você vai inserir? "))
   
    if numero_notas <= 0:
        raise ValueError("O número de notas deve ser positivo.")
    
    notas = []
    
    for i in range(numero_notas):
        nota = float(input(f"Digite a nota {i + 1}: "))
       
        validar_nota(nota)
        notas.append(nota)
    
    exibir_media(notas)
    
except ValueError as e:
   
    print(f"Erro: {e}")
finally:
    print("Programa finalizado.")