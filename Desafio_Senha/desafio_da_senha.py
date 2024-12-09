import random
import string


def gerandosenha(tamanho):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choices(caracteres, k=tamanho))
    return senha

def criptografar_senha(senha, deslocar):
    resultado = []
    
    for char in senha:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            n_char = chr((ord(char) - base + deslocar) % 26 + base)
        elif char.isdigit():
            n_char = chr((ord(char) - ord('0') + deslocar) % 10 + ord('0'))
        else:
            n_char = char
        
        resultado.append(n_char)
    
    return ''.join(resultado)


senhaoriginal = "A1b2C3d4"
senha_cripto = criptografar_senha(senhaoriginal, 3)

print(f"A senha original: {senhaoriginal}")
print("Senha criptografada:", senha_cripto)
