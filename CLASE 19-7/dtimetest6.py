"""Uso de la libreria datetime"""

"Operacion resta"

from datetime import datetime

datetime1 = datetime.strptime("01-07-2000 15:15:00", "%d-%m-%Y %H:%M:%S")
datetime2 = datetime.strptime("11-07-2000 11:55:00", "%d-%m-%Y %H:%M:%S")

tiempo = datetime2 - datetime1
print("La resta de fechas  es: {}".format(tiempo))