# Ejercicio 3.1. Escribir dos funciones que permitan calcular:
# a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
# b) La duración en horas, minutos y segundos de un intervalo dado en segundos.

def duracion_en_segundos(hr,min,seg):
    """Función que devuelve la duración en segundos dado un intervalo de horas, minutos y segundos"""
    return (hr*3600) + (min*60) + seg

# print(duracion_en_segundos(1,30,60))

def duracion_horas_minutos_segundos(seg):
    hr_entera = seg//3600
    hr = seg/3600
    resto_1 = hr-hr_entera

    min_entero = int(resto_1*60)
    min = resto_1*60
    resto_2= min-min_entero
    
    seg_entero = int(resto_2*60)
    return hr_entera, min_entero,seg_entero

# print(duracion_horas_minutos_segundos(4000))
    

    