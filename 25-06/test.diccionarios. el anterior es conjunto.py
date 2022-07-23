"""Introduccion a los diccionarios"""

"""Declarando nuestro primer diccionario"""

diccionario = {"nombre": "Carlos", "apellido": "Fernandez", "edad": 29}


print("El contenido de mi variable diccionario es: {}".format(diccionario))

print("Bienvenido {} {} usted tien {} años".format(diccionario['nombre'], diccionario['apellido'], diccionario['edad']))

diccionario2 = {"nombre": "Carlos", "apellido": "Fernandez", "cursos": ["Java", "SQL", "Django"]}

print("Los cursos a los que esta matriculado son {}".format(diccionario2["cursos"]))

print("1er curso: {}".format(diccionario2["cursos"][0]))
print("2do curso: {}".format(diccionario2["cursos"][1]))
print("3er curso: {}".format(diccionario2["cursos"][2]))

"""Adicional para introduccion a estructuras de control"""
i = 0
for key in diccionario2:
    if key =="cursos":
        for val in diccionario2[key]:
            print(diccionario2[key][i])
            i = i + 1  # Aumenta en 1 el valor de i
    