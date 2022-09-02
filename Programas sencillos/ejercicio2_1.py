def monto_final(pesos,tasa,años):
    """función que recibe una cantidad de pesos, una tasa de interés y un
número de años y devuelve el monto final a obtener"""
    resultado = pesos * ((1+(tasa/100))**años)
    return resultado

