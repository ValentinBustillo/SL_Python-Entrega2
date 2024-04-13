

def generar_estructura (nombre,gol,evitado,asistencia):
    lista_jugadores = []
    indice = 0
    for elem in nombre:
        lista_jugadores.append({'nombre': elem,'goles': gol[indice],'goles evitados': evitado[indice], 'asistencias':asistencia[indice]})
        indice += 1
    return lista_jugadores
