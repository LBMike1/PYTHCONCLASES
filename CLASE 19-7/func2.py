import random
"""funcion para pedir un numero"""
def cargar():
    return int(input("ingrese un numero: "))

def cargaraleatorio():
    return random.randint(1, 40)

"""Funcion para adivinar el numero"""
def adivinarnumero():
    numero = (cargaraleatorio())
    print("Adivina el numero!")

    esnumero = False
    while esnumero == False:
        x = cargar()
        if numero == x:
            print("Has ganado!!")
            esnumero = True
        elif numero<x:
            print("El valor ingresado es menor")
        else:
            print("El valor ingresado es mayor")