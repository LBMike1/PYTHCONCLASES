import random
"""Funcion para generar numeros aleatorios"""
def generarnumeros():
    lista = []
    for i in range(15):
        num = random.randint(1, 50)
        lista.append(num)
    return lista

"""Funcion para ordenar a lista"""
def ordenar(lista):
    return lista.sort()

"""Funcion para imprimir el valor de la lista"""
def imprimir(lista):
    print(lista)