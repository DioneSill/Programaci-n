def cuadrados(lista):
    lista_cuadrados = []
    for numero in lista: #Se recorre la lista
        lista_cuadrados.append(numero ** 2) #Cada numero lo eleva al cuadrado
    return lista_cuadrados #Devuelve la nueva lista

numeros = [2, 3, 4, 5]
resultado = cuadrados(numeros)
print("La lista es:", resultado)