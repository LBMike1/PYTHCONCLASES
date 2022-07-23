"""DECORADORES EN PYTHON"""

import time

def measuretime(func):
    def calculator(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)

        print("Tiempo de ejecucion total es: {}".format(time.time() - start))

        return result
    return calculator

@measuretime
def suma(a,b,c):
    time.sleep(1)
    resultado = a + b + c
    return resultado

def resta(a,b,c):
    time.sleep(1)
    resultado = a - b - c
    return resultado

print("La suma total es: {} ".format(suma(70,700,300)))
print("La resta total es: {} ".format(resta(70,700,300)))