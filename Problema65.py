def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numeros = []

while True:
    entrada = input("Ingresa un número (o escribe 'fin' para terminar): ")
    if entrada.lower() == "fin":
        break
    try:
        num = int(entrada)
        numeros.append(num)
        print(f"El factorial de {num} es {factorial(num)}")
    except ValueError:
        print("Por favor, ingresa un número válido")

print("Cantidad total de números leídos:", len(numeros))