"""Manejo de archivos"""

tecnologiasbackend = ["Python", "\njava", "\nRuby", "\nNodeJS"]

file= open("../myfiles/file4.txt", "a+")

file.writelines(tecnologiasbackend)

file = open("../myfiles/file4.txt", "r")

for newline in file:
    if newline.find("Python"):
        print("Tienes en tu lista a Python")
        #print(newline)

file.close()