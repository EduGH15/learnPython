# Ejercicio 3.4. Área de polígonos
# a) Escribir una función que reciba las coordenadas de un vector en ℝ3
# (x,y,z) y devuelva
# la norma del vector, dada por ‖⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ (𝑥, 𝑦, 𝑧)‖ = √𝑥
# 2 + 𝑦2 + 𝑧2.
# Ejemplo: norma(3, 2, -4) → 5.3851

import math

def norma_vector(x1,y1,z1):
    norma = round((x1**2 + y1**2 + z1**2)**0.5,4)
    return norma

# print(norma_vector(3,2,-4))

# b) Escribir una función que reciba las coordenadas de dos vectores en ℝ3
# (x1,y1,z1,x2,
# y2,z2) y devuelva las coordenadas del vector diferencia (debe devolver 3 valores numéricos).
# Ejemplo: diferencia(8, 7, -3, 5, 3, 2) → (3, 4, -5)

def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    dif_z = z1 - z2
    return dif_x, dif_y, dif_z

# c) Escribir una función que reciba las coordenadas de dos vectores en ℝ3 y devuelva las
# coordenadas del producto vectorial, definido como:

def producto_vectorial(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial"""
    x = y1*z2 - z1*y2
    y = - x1*z2 + x2*z1
    z = x1*y2 - y1*x2
    # print("DEBUGG === Valor de x:", x)
    # print("DEBUGG === Valor de y:", y)
    # print("DEBUGG === Valor de z:", z)
    return x,y,z

# ) Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de
# 3 puntos en ℝ3 y devuelva el área del triángulo que conforman.
# Ayuda: Si 𝐴, 𝐵 y 𝐶 son 3 puntos en el espacio, la norma del producto vectorial ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ 𝐴𝐵 × ⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗ 𝐴𝐶 es
# igual al doble del área del triángulo 𝐴𝐵𝐶.
# Ejemplo: area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) → 19.4551


def area_del_triangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3):
    """Recibe las coordenadas de 3 puntos en ℝ3 y devuelva el área del triángulo que conforman"""
    (u1,u2,u3) = diferencia(x2,y2,z2,x1,y1,z1)
    (v1,v2,v3) = diferencia(x3,y3,z3,x1,y1,z1)
    (coordenada1,coordenada2,coordenada3)=producto_vectorial(u1,u2,u3,v1,v2,v3)
    area = norma_vector(coordenada1,coordenada2,coordenada3)/2
    return area


# e) Escribir una función que reciba las coordenadas de 4 puntos en el plano ℝ2
# (x1,y1,x2,
# y2,x3,y3,x4,y4) que conforman un cuadrilátero convexo, y devuelva el área del mismo.
# Ayuda: Aprovechar las funciones escritas anteriormente, asumiendo que los puntos dados
# están en ℝ3
# con coordenada 𝑧 = 0.
# Ejemplo: area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5) → 65

def area_cuadrilatero(x1,y1,x2,y2,x3,y3,x4,y4):
    (u1,u2,u3) = diferencia(x2,y2,0,x1,y1,0)
    (v1,v2,v3) = diferencia(x3,y3,0,x1,y1,0)
    (w1,w2,w3) = diferencia(x4,y4,0,x1,y1,0)

    (coordenada1,coordenada2,coordenada3)=producto_vectorial(u1,u2,u3,v1,v2,v3)
    area1 = (norma_vector(coordenada1,coordenada2,coordenada3)/2)

    (coordenada4,coordenada5,coordenada6)=producto_vectorial(v1,v2,v3,w1,w2,w3)
    area2 = (norma_vector(coordenada4,coordenada5,coordenada6)/2)

    return int(area1+area2)
     


# print(area_cuadrilatero(1,2,5,4,7,10,1,3))
print(area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5))


