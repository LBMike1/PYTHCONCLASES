"""Uso de **args"""



def multiplicar(*args):
    valor = 1
    for i in args:
        print(i)
        valor = valor * i
    return valor


num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
print("EL resultado total es: {}".format(multiplicar(num1,num2)))
