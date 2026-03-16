def llenar_lista():
    lista = []
    for _ in range(3): 
        lista.append(int(input("Ingresa un número: ")))
    return lista

numeros = llenar_lista()
print("Tu lista es:", numeros)