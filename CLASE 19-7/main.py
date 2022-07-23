"""Desarrollar un programa que pueda generar 15 numeros aleatorios entre 1 y 50
Reglas:
1. Mostrar la lista con los numeros que se han obtenido
2. Ordenar los valores de la lista e imprimirlos en pantalla
3. Modularizar o dividir en funciones.
"""

#import func

#print(func.generarnumeros())

from func import *

miLista = generarnumeros()
imprimir(miLista)
ordenar(miLista)
imprimir(miLista)

