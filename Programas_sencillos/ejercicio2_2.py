# Utilizando la función del ejercicio anterior, escribir un programa que le pregunte
# al usuario la cantidad de pesos inicial, la tasa de interés y el número de años y muestre el monto
# final a obtener.

from ejercicio2_1 import monto_final

pesos = int(input("ingrese un capital:"))
tasa = int(input("Ingrese una tasa de interés:"))
años = int(input("Ingrese una cantidad de años:"))

input(monto_final(pesos,tasa,años))
