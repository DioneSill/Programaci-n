def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def llenar_lista():
    lista = []
    for _ in range(3):  
        lista.append(int(input("Ingresa un número: ")))
    return lista

numeros = llenar_lista()
resultado = sumar_lista(numeros)
print("La suma de la lista es:", resultado)