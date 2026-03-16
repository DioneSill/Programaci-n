def calificaciones(a, b, c):
    return (a+b+c)/3 #importante unir las cantidades

a = int(input("Ingrese una calificacion: "))
b = int(input("Ingrese una calificacion: "))
c = int(input("Ingrese una calificacion: "))

resultado = calificaciones( a, b, c) 
if resultado < 70:
    print("Tu promedio es:", resultado, "estas reprobado, te vas a extras")
else:
    print("Tu promedio es:", resultado, "estas aprobado")
