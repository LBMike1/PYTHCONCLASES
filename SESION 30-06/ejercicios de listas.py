""""Ejercicios de listas"""

"""Crear una lista con 10 valores aleatorios"""

"""Ordenar una lista de menor a mayor"""

import random

milista = []

for indice in range(1,11):
    milista.append(random.randint(10,100))

listanueva = milista.sort()

"""va a imprimir numeros aleatorios entre 10 al 100"""

print("Mi lista actual es: {}".format(milista))
print("Mi lista ordenada es: {}".format(milista))

for numero in milista:
    print(numero)


