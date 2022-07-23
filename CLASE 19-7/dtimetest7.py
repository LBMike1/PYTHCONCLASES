"""Uso de la libreria datetime"""
"""Usando la funcion stprtime"""

from datetime import datetime

print("La fecha actual es: {}".format(datetime.now()))

date = datetime.strptime("01-07-2000 15:15:00", "%d-%m-%Y %H:%M:%S")

print(date.strftime("%d del %m del año %Y con las %H y %M minutos"))