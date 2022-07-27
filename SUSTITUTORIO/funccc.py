
from datetime import date, time, datetime

import datetime
import random


def cargar():
    return int(input("ingrese un numero: "))

def cargaraleatorio():
    return random.randint(1, 30)

def fechayhora():
    return datetime.datetime.now()



def adivinarnumero():
    numero = (cargaraleatorio())
    print("Adivina el numero!")


    esnumero = False

    while esnumero == False:


        x = cargar()

        if 0 < x < 100:
            print("Vas bien")
        elif x > 100:
            print("El numero ingresado no es válido")


        if numero == x:
            print("Has ganado!!")
            print("El momento exacto que adivinaste fue a las : {}".format(fechayhora()))

            esnumero = True


        elif numero<x:
            print("El valor ingresado es menor")
        else:
            print("El valor ingresado es mayor")






