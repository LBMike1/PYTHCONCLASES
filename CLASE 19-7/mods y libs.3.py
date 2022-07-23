"""Importacion y uso de librerias"""

"""Uso especifico de una funcionalidad para una libreria o dependencia"""

from math import sqrt as raiz, pow as potencia
import math
numero = int(input("Por favor ingrese un numero: "))

valorRaiz = raiz(numero)
print("La raiz cuadrada de un numero ingresado es: {}".format(valorRaiz))

valorPotencia = potencia(numero, 22)

print("El valor de mi potencia es: {}".format(valorPotencia))

print("todas las funciones que tiene la libreria math son: {}".format(dir(math)))