"""DECORADORES EN PYTHON"""
"""Creacion de una funcion decoradora"""

def funcionA(funcionB):
    def funcionc(*args, **kwargs):
        print("Antes de ejecutar la funcion que pasa por parametro")
        resultado = funcionB(*args,**kwargs)
        print(resultado)
        print("Despues de ejecutar la funcion decoradora")

    return funcionc

@funcionA
def suma(a,b,c,d):
    total = a + b + c + d
    return total

suma(50,56,50,12)