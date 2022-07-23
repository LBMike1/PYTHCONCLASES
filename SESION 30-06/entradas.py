"""Entradas y salidas con Python"""


"""Entradas en Python"""

usuario = input("Ingrese su nombre de usuario: ")
nombre = input("¿Cual es su nombre?: ")

print("¡Bienvenido: {}!".format(nombre))

telefono = input("Ingrese su numero de celular: ")

print("{} tiene el numero telefonico: {}".format(nombre,telefono))
"""edad convertida a entero con int"""
edad = int(input("¿Cual es su edad?: "))

print(type(edad))

print("Usted tiene {} años".format(edad))

if edad<18:
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")
