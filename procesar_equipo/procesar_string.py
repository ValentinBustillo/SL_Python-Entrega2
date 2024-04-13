
def acomodar_lista (string):
    lista = string.replace(',','').split()
    lista1 = []
    for elem in lista:
        lista1.append(elem.capitalize())
    return lista1