
def conocer_goleador (lis):
    nombre_goleador = ''
    goles_goleador = ''
    prom_goles_por_partido = 0
    max_goles = 0
    for elem in lis:
        if elem['goles'] > max_goles:
            nombre_goleador = elem['nombre']
            goles_goleador = elem['goles']
            max_goles = elem['goles']
    goleador = {'nombre': nombre_goleador, 'goles': goles_goleador}
    return goleador