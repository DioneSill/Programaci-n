def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def verificar_primo():
    numero = int(input("Ingresa un número para verificar si es primo: "))
    if es_primo(numero):
        print(f"{numero} es primo")
    else:
        print(f"{numero} NO es primo")

verificar_primo()