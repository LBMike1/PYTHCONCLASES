""""Bucle while"""
"El # nos permite ingresar texto al lado de una variable sin afectarla"

numero = int(input("Ingrese un numero menor de 10: "))

while numero < 10:
    numero += 1 #Aumenta en uno el valor de la variable "numero"
    print("El numero es: {}".format(numero))
    if numero == 8:
        print("numero encontrado!")
        break #El break nos permite terminar el bucle antes que llegue al tope de la condicion

print("Llegó al final del bucle while")


