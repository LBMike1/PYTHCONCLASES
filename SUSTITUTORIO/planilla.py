class Persona ():

    def __init__(self,nombre,edad):
        self._nombre = input("Introduzca su nombre: ")
        self.edad = int(input("Introduzca su edad: "))

    def imprimir(self):
        print("Nombre del empleado: {}".format(self._nombre))
        print("Edad del empleado: {}".format(self.edad))
        print("Sueldo del empleado: {}".format(self.sueldo))

class Empleado(Persona):

    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = int(input("Introduzca su sueldo: "))

    def impuesto(self):
        self.sueldo = self.sueldo
        impuesto = self.sueldo * 0.10
        if self.sueldo >= 2000:

            print("Debera pagar un impuesto de: {} ".format(impuesto))

        else:
            print("No pagará impuesto")


    def manejodiccionario(self):
        valores = {"nombre": self._nombre,"edad": self.edad, "sueldo": self.sueldo, "impuesto": self.impuesto()}
        print(valores)


    def generararchivoempleado(self):
        valores = {"nombre": self._nombre, "\nedad": self.edad, "\nsueldo": self.sueldo, "\nimpuesto": self.impuesto()}
        lista = list(valores.values())
        for nombre in lista:
            print(nombre)
        file = open("./myfiles/planilla.txt", "a+")

        file = open("./myfiles/planilla.txt", "r")
        print("El contenido de nuestro archivo es: {}".format(file.read()))
        file.close()

empleado1 = Empleado(" ", ''," ")
empleado1.imprimir()
#empleado1.manejodiccionario()
empleado1.generararchivoempleado()


