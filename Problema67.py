
def ordena_creciente(lista):
    return sorted(lista)

def ordena_decreciente(lista):
    return sorted(lista, reverse=True)

def elimina_por_indice(lista, indice):
    if 0 <= indice < len(lista):
        return lista.pop(indice)
    else:
        return None  

def elimina_por_dato(lista, dato):
    if dato in lista:
        lista.remove(dato)
    return lista

def estadisticas(lista):
    promedio = sum(lista) / len(lista) if len(lista) > 0 else 0
    maximo = max(lista) if lista else None
    minimo = min(lista) if lista else None
    return promedio, maximo, minimo


entrada = input("Ingresa los números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

print("\nLista original:", numeros)

print("Orden creciente:", ordena_creciente(numeros))


print("Orden decreciente:", ordena_decreciente(numeros))


indice = int(input("\nIngresa un índice para eliminar: "))
valor_eliminado = elimina_por_indice(numeros, indice)
print(f"Valor eliminado por índice {indice}: {valor_eliminado}")
print("Lista actual:", numeros)


dato = int(input("\nIngresa un dato para eliminar de la lista: "))
numeros = elimina_por_dato(numeros, dato)
print("Lista después de eliminar", dato, ":", numeros)

prom, maximo, minimo = estadisticas(numeros)
print(f"\nPromedio: {prom}, Máximo: {maximo}, Mínimo: {minimo}")