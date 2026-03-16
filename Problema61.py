def base_altura(a,b):
    return 2*a + 2*b

a = int(input("Ingresa la base del rectángulo: "))
b = int(input("Ingresa la altura del rectángulo: "))

resultado = base_altura(a, b)
print("El perimetro del rectangulo es: ", resultado)