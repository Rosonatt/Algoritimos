def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente-1)


resultado = potencia(2, 3)
print(resultado)
