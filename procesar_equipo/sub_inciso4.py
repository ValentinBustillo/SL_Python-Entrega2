
def prom_goles_equipo (lista_goles):
    cuantos_goles = 0
    for elem in lista_goles:
        cuantos_goles += elem
    prom = cuantos_goles / 25
    return prom