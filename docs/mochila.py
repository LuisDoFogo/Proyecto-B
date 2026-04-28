#mochila.py

def mochila_fraccionaria(objetos, capacidad):
    """
    objetos = lista de tuplas (peso, ganancia)
    capacidad = peso máximo permitido

    Retorna:
    valor_total
    seleccion = lista con fracciones tomadas
    """

    # Calculamos ganancia/peso
    objetos_ordenados = []

    for peso, ganancia in objetos:
        relacion = ganancia / peso
        objetos_ordenados.append((peso, ganancia, relacion))

    # Ordenar de mayor a menor según ganancia/peso
    objetos_ordenados.sort(key=lambda x: x[2], reverse=True)

    valor_total = 0
    seleccion = []

    for peso, ganancia, relacion in objetos_ordenados:
        if capacidad >= peso:
            # Tomamos el objeto completo
            capacidad -= peso
            valor_total += ganancia
            seleccion.append((peso, ganancia, 1))
        else:
            # Tomamos una fracción
            fraccion = capacidad / peso
            valor_total += ganancia * fraccion
            seleccion.append((peso, ganancia, round(fraccion, 2)))
            break

    return round(valor_total, 2), seleccion