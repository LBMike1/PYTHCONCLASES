"""Manejo de archivos"""

def filemanipulation(dir, mode):
    try:
        file = open(dir,mode)
        print(file.read())
        file.close
        return file
    except OSError as err:
        print("Error de lectura {}".format(err))

filewrite = "../myfiles/files2.txt"

print("Lectura de un archivo")

filemanipulation(filewrite, "r")

filewrite2 = "../myfiles/APPEND.txt"

filemanipulation(filewrite2, "a+")