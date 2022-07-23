"""Asignacion multiple"""

"""Referente a dos o mas variables"""

nombre = input("¿Cual es su nombre?: ")
correo = input("Digite su correo electronico: ")
edad = input("¿Cual es su edad?: ")
"""asignacion multiple: en una sola linea diferentes variables  """
nombreUsuario, correoUsuario,edadUsuario = nombre, correo, edad

print("El nombre de usuario es: {}".format(nombreUsuario))
print("Correo: {}".format(correoUsuario))
print("Edad: {}".format(edadUsuario))

