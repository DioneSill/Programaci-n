def EsMultiplo(a, b):
    return a, b

a = int(input("Ingresa un numero:"))
b = int(input("Ingresa un numero:"))

if a % b == 0:
    print("Es multiplo")
else:
    print("No es multiplo")