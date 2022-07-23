"""Manejo de excepciones"""

"""Para controlar el error de division entre cero y el tipo de datos"""
"""Multiples excepts en uno solo"""

try:
    #valor = 500/0
    suma = 12081 + "Hola!!"

except (ZeroDivisionError,TypeError):
    print("Ha ocurrido un error de DivisionZero o TypeError")