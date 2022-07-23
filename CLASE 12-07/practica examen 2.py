""""Ejercicio 2 de clases de python"""

"""
2.Crear un programa que tenga la clase Persona.
Reglas:
- La clase tendra como atributos el nombre y la edad de una persona
- Implementar los metodos para inicializar los atributos
- Implementar un metodo para mostrar e indicar si la persona es mayor de edad


"""

class Persona ():
    """Inicializar los atributos en el constructor"""
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrardatos(self):
        print("Su nombre es: {}".format(self.nombre))
        print("Y su edad: {}".format(self.edad))

        """Metodo para obtener el resultado"""

    def mayoredad(self):
        if self.edad >= 18:
                print("La persona es mayor de edad")

        else:
                print("La persona es menor de edad")

"""Creando las nuevas instancias"""
persona1 = Persona("Sofia",20)
persona2 = Persona("Juan",10)


persona1.mostrardatos()
persona1.mayoredad()

persona2.mostrardatos()
persona2.mayoredad()