import random

def generarnumeros():
    lista = []
    for i in range(10):
        num = random.randint(1, 100)
        lista.append(num)
    return lista


