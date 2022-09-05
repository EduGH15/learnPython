# Ejercicio 2.6. Escribir un programa que imprima todos los números pares entre dos números
# que se le pidan al usuario.

inicio= int(input("ingrese un número:"))
fin = int(input("ingrese otro número:"))
def intervalo_numeros_pares(inicio, fin):
    for i in range (inicio, fin+1):
        if(i%2==0):
            print(i)

intervalo_numeros_pares(inicio,fin)
