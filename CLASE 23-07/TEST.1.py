"""DECORADORES EN PYTHON"""

def funcionA(funcionB):
    "Funcion interna de la funcion decoradora"

    def funcionC():
        print("1. Antes de ejecutar la funcion decorar\n")
        #funcionB()
        print("\n2.Despues de ejecutar la funcion decorar ")


    return funcionC()

@funcionA
def saludar():
    print("Hola Pythonista")