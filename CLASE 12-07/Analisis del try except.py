"""Manejo de excepciones"""
"""Analisis del try except"""


try:
    #Valor1 = 10012/4
    Valor2 = 10012 / 0
except:
    print("Entro al except. Ha caido en excepcion")

else:
    print("Entro en else, no ha ocurrido un error")