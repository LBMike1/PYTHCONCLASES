
"""Manejo de archivos"""
"""Apertura y lectura de archivos"""

"""r: Abre el archivo en solo lectura"""
file = open("../myfiles/file.txt", "r")

"""read(): nos permite leer el contenido de un archivo"""
print("El contenido de nuestro archivo es: {}".format(file.read()))