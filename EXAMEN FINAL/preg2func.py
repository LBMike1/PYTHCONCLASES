import random
from math import sqrt
def generarnumeros():
    lista = []
    for i in range(15):
        num = random.randint(1, 50)
        lista.append(num)
    return lista


#def ordenar(lista):
    #print("Mi lista ordenada es: ".format(lista.sort()))

def tamaño(lista):
    print("El tamaño de mi lista es: ".format(len(lista)))

def imprimir(lista):
    print(lista)
def generaraiz():
    raiz = sqrt(lista)
    print(raiz)



