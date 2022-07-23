
"""Manejo de archivos"""
"""Apertura y lectura de archivos"""

"""w: Abre el archivo para poder escribir sobre el"""

file = open("../myfiles/files2.txt", "w")

file.write("Lenguaje multiplataforma")
file.write("\nEsta basado")

file = open("../myfiles/files2.txt", "r")
print("El contenido de nuestro archivo es: {}".format(file.read()))

"""CIERRE DEL ARCHIVO"""
file.close()

