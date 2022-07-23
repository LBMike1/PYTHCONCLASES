"""uso del for"""

ingenierias = ["software", "sistemas", "agronoma", "industrial","quimica", "ambiental"]
i = 0
print("El tamaño de nuestra lista es: {}".format(len(ingenierias)))

for ingenieria in ingenierias:

    print("Ingenieria {}".format(ingenieria))

    i = i + 1
    print("esta la vuelta numero: {}".format(i))