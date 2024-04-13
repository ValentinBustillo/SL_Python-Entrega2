import info
from procesar_equipo import procesar_string
from procesar_equipo import sub_inciso1
from procesar_equipo import sub_inciso2
from procesar_equipo import sub_inciso3
from procesar_equipo import sub_inciso4
from procesar_equipo import sub_inciso5


def main():
    nombres = procesar_string.acomodar_lista(info.names)
    lista = sub_inciso1.generar_estructura(nombres, info.goals, info.goals_avoided,info.assists)
    goleador = sub_inciso2.conocer_goleador(lista)
    influyente = sub_inciso3.conocer_jugador_influyente(lista)
    promedio_equipo = sub_inciso4.prom_goles_equipo(info.goals)
    promedio_goleador = sub_inciso5.promedio_goles(goleador)
    print(f'El goleador del equipo es {goleador}')
    print(f'El jugador influyente es {influyente}')
    print(f'El promedio de goles por partido del equipo es {promedio_equipo}')
    print(f'El promedio de goles por partido del goleador del equipo es {promedio_goleador}')

main()