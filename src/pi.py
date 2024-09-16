#!/usr/bin/env python
def imagen_func(punto): #sirve para evaluar el valor en "y" de un punto "x".
   return 4/(1+punto**2)

def riemann(limite_inferior, limite_superior, cant_rectangulos, imagen_punto):
    distancia = (limite_superior-limite_inferior)/cant_rectangulos #evalúa la medida de las bases de los rectángulos.
    punto_medio = limite_inferior + distancia/2 #es el punto medio del primer rectángulo.
    sumatoria_area = 0.0 #va a sumar el área de cada rectángulo.
    for rectangulo in range(cant_rectangulos): 
        if rectangulo != 0: #para el primer rectángulo ya está evaluado el punto medio, por eso se excluye.
            punto_medio += distancia #evalúa el punto medio del rectángulo que se está evaluando.
        sumatoria_area += imagen_punto(punto_medio)*distancia #calcula el área del rectángulo y lo mete en la sumatoria.
    return sumatoria_area #devuelve la suma de todos los rectángulos sumados (un valor aproximado de la integral).
   
print(riemann(0, 1, 1000000, imagen_func))

