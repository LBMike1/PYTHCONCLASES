"""Manejo de archivos"""

tecnologiasbackend = ["Python", "java", "Ruby", "NodeJS"]
tecnologiasfrontend = ["Angular", "Javascript","AngularJS", "bootstrap"]

"""apertura de nuestro archivo"""

#a+ permite escribir varias lineas de codigo al abrir nuestro archivo
#escribe unas lineas de texto sin sobreescribir el contenido del archivo
file= open("../myfiles/file3.txt", "a+")
#Los puntos sirven para extraer el archivo de una carpeta o subcarpeta
file.writelines(tecnologiasfrontend)
file.writelines(tecnologiasbackend)

file = open("../myfiles/file3.txt", "r")

print("El contenido de nuestro archivo es: {}".format(file3.read()))

"""CIERRE DEL ARCHIVO"""
file.close()


