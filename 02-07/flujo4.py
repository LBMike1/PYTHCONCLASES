"""Creacion de una lista"""
"""una variable que contenta 30 numeros aleatorios"""
"""Mostrar los valores al cuadrado y al cubo de los datos de la lista Random"""

import random
listaRandom = []

for indice in range(30):
    listaRandom.append(random.randint(0, 78))
print(listaRandom)
"""Obtener el tamaño de mi lista"""

print("El tamaño de mi lista es: {}".format(len(listaRandom)))
"""Para elevar al cuadrado y al cubo"""
valor1 = 3**2
valor2 = 3**3

for valor in listaRandom:
    print("El valor al cuadrado es: {} y el valor al cubo es: {} ".format(valor**2,valor**3))

for indice in range(30):
    val = random.randint(5, 20)
    print("Numero random original: {}".format(val))
    print("cuadrado: {} y al cubo es: {}".format(val**2, val**3))

val111 = 40.8

print("Nuevo valor: {}".format(int(val111)))

VAL111111 = 39%10

print(format(VAL111111))



