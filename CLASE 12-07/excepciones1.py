"""Manejo de excepciones"""

"""Para controlar el error de division entre cero y el tipo de datos"""

try:
    vall = 100/0
    suma = 10000 + "Hola pythonistas"

except ZeroDivisionError:
    print(" No es posible una division entre cero!!")
except TypeError:
    print("No es posible sumar un tipo de dato entero y tipo string")