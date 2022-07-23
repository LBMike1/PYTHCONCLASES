"""Bucle while"""


"""Leer por teclado enteros positivos"""

"""imprimir la suma de todos los digitos que lo componen"""

""""""

numero = int(input("Ingrese un numero positivo: "))

while numero != 0:
    digito = numero % 10
    suma = digito + numero
    numero = numero //10
    print("digito: {}".format(digito))
    print("suma: {}".format(suma))
    print("numero: {}".format(numero))

print("LA suma de los digitos es: {}".format(suma))





print("La suma de los digitos es: {}".format(suma))