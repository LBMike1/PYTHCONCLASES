""""Ejercicio 3 de clases de python"""

"""
4.Crear un programa el cual pueda declarar los valores enteros por teclado.
Crear un programa que  pueda realizar depositos y extracciones de dinero

Reglas:

- El banco va a requerir que al finalizar el dia calcule el dinero que se ha depositado
- Crear dos clases, una clase cliente y otra clase banco.
- La clase cliente tendra los atributos de nombre y cantidad
- Crear los metodos constructor, depositar, extraer, mostrar el total de dinero depositado
- El banco tendra 3 atributos de la clase cliente, el metodo constructor operar y deposito total
- Instanciar para el caso de 3 personas
-

"""""

class Banco:

    def __init__(self):
        self.cliente1 = Cliente("Susana")
        self.cliente2 = Cliente("Jireh")
        self.cliente3 = Cliente("Juana")

    def operar(self):
        self.cliente1.depositar(500)
        self.cliente2.depositar(129341)
        self.cliente3.depositar(89192)
        self.cliente1.retirar(40)
        self.cliente2.retirar(4412)
        self.cliente3.retirar(89192)

    def depositos(self):
        total = self.cliente1.mostrartotal() + self.cliente2.mostrartotal() + self.cliente3.mostrartotal()
        print("El total de dinero que tiene el banco es: {}".format(total))
        self.cliente1.imprimirdatos()
        self.cliente2.imprimirdatos()
        self.cliente3.imprimirdatos()


class Cliente:

    def __init__(self,nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        self.cantidad += monto

    def retirar(self, monto):
        self.cantidad -= monto

    def mostrartotal(self):
        return self.cantidad

    def imprimirdatos(self):
        print("{} Tiene una cantidad depositada de : {}".format(self.nombre, self.cantidad))

banco = Banco()
banco.operar()
banco.depositos()