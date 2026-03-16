def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def promedio_lista(lista):
    total = sumar_lista(lista)      
    cantidad = len(lista)           
    return total / cantidad         


def llenar_lista():
    lista = []
    for i in range(3): 
        lista.append(int(input("Ingresa un número: ")))
    return lista

numeros = llenar_lista()
prom = promedio_lista(numeros)
print("El promedio de la lista es:", prom)