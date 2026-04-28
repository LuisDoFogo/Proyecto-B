#monedas 

def cambio_monedas(denominaciones, cantidad):
    """
    denominaciones = lista de monedas disponibles
    cantidad = cantidad objetivo

    Retorna:
    mínimo número de monedas
    combinación óptima
    """

    max_valor = float('inf')

    dp = [max_valor] * (cantidad + 1)
    dp[0] = 0

    usada = [-1] * (cantidad + 1)

    for moneda in denominaciones:
        for i in range(moneda, cantidad + 1):
            if dp[i - moneda] + 1 < dp[i]:
                dp[i] = dp[i - moneda] + 1
                usada[i] = moneda

    if dp[cantidad] == max_valor:
        return "No posible", []

    combinacion = []
    while cantidad > 0:
        combinacion.append(usada[cantidad])
        cantidad -= usada[cantidad]

    return dp[len(dp) - 1], combinacion