def obtener_reprobados(nombres, calificaciones):
    reprobados = []
    for i in range(len(nombres)):
        if calificaciones[i] < 70: 
            reprobados.append(nombres[i])
    return reprobados

nombres = ["Ana", "Luis", "Carla", "Pedro"]
calificaciones = [85, 60, 72, 50]

reprobados = obtener_reprobados(nombres, calificaciones)
print("Los alumnos reprobados son:", reprobados)