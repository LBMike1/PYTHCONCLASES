from datetime import datetime

tiempoahora = datetime.strptime("23/07/2022 14:12:44", "%d/%m/%Y %H:%M:%S").timestamp()

print("La conversion de nuestro tiempo ahora es: {}".format(tiempoahora))


