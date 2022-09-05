# a) Escribir una función que dado un número entero devuelva 1 si el mismo
# es impar y 0 si fuera par.

# def es_par(nro):
#     if(nro%2 == 0):
#         return 0
#     else:
#         return 1

# print(es_par(0))
# print(es_par(2))
# print(es_par(3))

# b) Escribir una función que dado un número entero devuelva 0 si el mismo es impar y 1 si
# fuera par.

# def es_par_v2(nro):
#     if(nro%2 == 0):
#         return 1
#     else:
#         return 0

# print(es_par_v2(0))
# print(es_par_v2(2))
# print(es_par_v2(3))

# c) Escribir una función que dado un número entero devuelva el dígito de las unidades. Por
# ejemplo, para 153 debe devolver 3.

# def longitud(nro):
#     return len(str(nro))

# Escribir una función que dado un número devuelva el primer número múltiplo de 10
# inferior a él. Por ejemplo, para 153 debe devolver 150.

def multiplo_de_10(nro):
    lista = []
    for i in range(0,nro+1):
        if(i%10==0):
            lista.append(i)
    print(lista[-1])
# multiplo_de_10(239)

