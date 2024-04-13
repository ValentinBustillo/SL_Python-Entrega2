
def conocer_jugador_influyente(lis):
    porcentaje = 0
    procentaje_max = 0
    nombre_max = ''
    for elem in lis:
        porcentaje = (elem['goles'] * 1.5) + (elem['goles evitados'] * 1.25) + elem['asistencias']
        if porcentaje > procentaje_max:
            porcentaje_max = porcentaje
            nombre_max = elem['nombre']
    mas_influyente = {'nombre':nombre_max, 'porcentaje':porcentaje_max}
    return mas_influyente