"""DECORADORES EN PYTHON"""
"""Creacion de una funcion decoradora"""
def funcionA(funcionB):
    def funcionc(*args,**kwargs):
        print("1. Antes de ejecutar la funcion decorar\n")
        resultado = funcionB(*args,**kwargs)
        print("\n2.Despues de ejecutar la funcion decorar ")
        return resultado
    
@funcionA
def saludar(name,lastname,age):

    return print("Hola {} {} usted tiene {} años".format(name,apellido,edad))

nombre = input("Ingrese su nombre por favor: ")
apellido = input("Ingrese su apellido por favor: ")
edad = input("Ingrese su edad por favor: ")
saludar(nombre,apellido,edad)


