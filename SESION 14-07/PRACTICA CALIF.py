
"""1. Escriba un programa donde tendrá los siguientes requisitos:
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad y de nacionalidad peruana (use el manejo de errores para el tipo de
dato)
- Un método cumpleaños donde cada vez que invoque aumentará en un año la
edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo 2 vez, mostrar por pantalla dicha edad
actualizada).
-- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla)"""""

class Persona:

    def __init__(self,nombre,edad,nacionalidad,saldo):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.saldo = 0

    def cumpleaños(self):
        self.cumpleaños = self.edad + 1
    def otrocumpleaños(self):
        self.cumpleaños = self.edad + 2


    def transferencia(self,persona2):
        self.saldo =+ monto

def sumarDigito(numero):
    suma=0
    while numero!=0:
        digito =numero%10
        suma = suma+digito
        numero = int(numero/10)
    return suma

def dividirDigito(numero):
    division = num/num2
    while numero!=0:
        digito =numero%10
        numero = int(numero/10)
    return division



num = int(input("Ingrese número a procesar: "))
num2 = int(input("Ingrese número a procesar: "))
while num!=0:
    print("Suma {}".format(sumarDigito(num)))
    num = int(input("Ingrese número a procesar: "))
while num2!=0:
    print("Suma {}".format(sumarDigito(num)))
    num = int(input("Ingrese número a procesar: "))
while num!=0:
    print("Division {}".format(dividirDigito(num)))
    num = int(input("Ingrese número a procesar: "))
while num2!=0:
    print("Division {}".format(dividirDigito(num)))
    num = int(input("Ingrese número a procesar: "))

try:
    valor = num/0


except (ZeroDivisionError,TypeError):
    print("Ha ocurrido un error de DivisionZero o TypeError")


