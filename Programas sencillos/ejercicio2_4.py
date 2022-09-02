#  Escribir un programa que utilice la función anterior para generar una tabla de
# conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10

from ejercicio2_3 import convertir_fahrenheit_celsius

def mostrar_tabla_grados():
    for i in range(0,121,10):
       C = convertir_fahrenheit_celsius(i)
       print(i, "--->", C)

mostrar_tabla_grados()
    
