from ejercicio3_1 import *

horas_1 = int(input("Ingrese una cantidad de horas:"))
minutos_1 = int(input("Ingrese una cantidad de minutos:"))
segundos_1 = int(input("Ingrese una cantidad de segundos:"))

horas_2 = int(input("Ingrese otra cantidad de horas:"))
minutos_2 = int(input("Ingrese otra cantidad de minutos:"))
segundos_2 = int(input("Ingrese otra cantidad de segundos:"))

def duracion_total(horas_1,minutos_1,segundos_1,horas_2,minutos_2,segundos_2):
    valor_1 = duracion_en_segundos(horas_1,minutos_1,segundos_1)
    print(valor_1)
    valor_2 = duracion_en_segundos(horas_2,minutos_2,segundos_2)
    print(valor_2)
    valor_3 = valor_1 + valor_2
    print(valor_3)
    return duracion_horas_minutos_segundos(valor_3)

print(duracion_total(horas_1,minutos_1,segundos_1,horas_2,minutos_2,segundos_2))






