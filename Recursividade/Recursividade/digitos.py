def digitos(num):
    if num < 10:
        return 1
    return 1 + digitos(num // 10)


resultado = digitos(555)
print(resultado)
