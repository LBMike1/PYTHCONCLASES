import time

def measuretime(func):
    def calculator(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)

        print("Tiempo de ejecucion total es: {}".format(time.time() - start))

        return result
    return calculator

@measuretime
def division(a,b):
    time.sleep(1)
    resultado = a / b
    return resultado

print("La division total 1 es: {} ".format(division(500,20)))
print("La division total 2 es: {} ".format(division(651,200)))
print("La division total 3 es: {} ".format(division(199123,2563)))