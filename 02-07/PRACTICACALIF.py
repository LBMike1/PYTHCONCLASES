"""EJERCICIO 1"""

nombre = input("Buenos dias/tardes, ¿Cuál es su nombre: ")
apellido = input("¿Cual es su apellido?: ")
edad = int(input(("¿Cual es edad?: ")))

print("El tipo de variable del nombre es: {}".format(type(nombre)))
print("El tipo de variable del apellido es: {}".format(type(apellido)))
print("El tipo de variable de la edad es: {}".format(type(edad)))


nombre2 = input("Buenos dias/tardes, ¿Cuál es su nombre: ")
apellido2 = input("¿Cual es su apellido?: ")
edad2 = int(input(("¿Cual es edad?: ")))

print("El tipo de variable del nombre es: {}".format(type(nombre2)))
print("El tipo de variable del apellido es: {}".format(type(apellido2)))
print("El tipo de variable de la edad es: {}".format(type(edad2)))

suma = edad + edad2
print("La suma de las edades del primer y segundo trabajador es: {}".format(suma))

""""EJERCICIO 2"""
import random
listarandom = []

for indice in range(10):
    listarandom.append(random.randint(0,100))
print(listarandom)

valor1 = 3**2
valor2 = 3**3
for valor in listarandom:
    print("El valor al cuadrado es: {} y el valor al cubo es: {} ".format(valor**2,valor**3))

"""EJERCICIO 3"""

diccionario = {"nombre": "Jorge", "apellido": "Rojas", "edad": 42, "DNI": "78675645"}

"""Obteniendo los valores de un key en especifico"""

var1 = diccionario["nombre"]
var2 = diccionario["apellido"]
var3 = diccionario["edad"]
var4 = diccionario["DNI"]

print("El valor de mi key 'nombre' es: {}".format(var1))
print("El valor de mi key 'apellido' es: {}".format(var2))
print("El valor de mi key 'edad' es: {}".format(var3))
print("El valor de mi key 'DNI' es: {}".format(var4))

list(diccionario)

print("El valor de mi diccionario convertido a lista es: {}".format(list(diccionario)))

del diccionario["DNI"]

print("Mi diccionario actualizado es: {}".format(diccionario))

diccionario["profesion"] = "Asistente"

print("El valor de mi nuevo diccionario es: {}".format(diccionario))