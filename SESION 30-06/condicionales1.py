"""Uso del flujo condicional"""

edad = int(input("Cual es su edad?: "))

if 0<edad<18:
    print("Es usted menor de edad")

elif 18<= edad < 120:
    print("Usted es mayor de edad")

elif 60< edad < 120:
    print("Ya estas cochit@")
else:
    print("Ya estas robando aire")