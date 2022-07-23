"""Funcion principal"""

"""LLama a las demas funciones de mi modulo externo"""

from funciones import *

x = int(input("ingrese un valor: "))
y = int(input("ingrese un segundo valor: "))

print("El resultado de la suma de los valores ingresados es: {}".format(suma(x,y)))

print("El resultado de la multiplicacion de los valores ingresados es: {}".format(multiplicacion(x,y)))

print("El resultado de la resta de los valores ingresados es: {}".format(resta(x,y)))