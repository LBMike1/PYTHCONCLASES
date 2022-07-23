"""uso de la libreria de fechas y tiempos"""
"""Conversion total del tiempo"""

from datetime import datetime

"""
H: HORA
M: MINUTO
S: SEGUNDOS
"""

timeNow = datetime.strptime("2023/03/15 20:40:00", "%Y/%m/%d %H:%M:%S").timestamp()

print("La conversion de nuestro valor de tiempo es: {}".format(timeNow))

""""""

"""Obtendremos la cantidad total en segundos usando: timestamp"""
timeNow = datetime.strptime("2023/02/01 20:40:00", "%Y/%m/%d %H:%M:%S").timestamp()

print("La conversión de nuestro valor en tiempo es: {}".format(timeNow))