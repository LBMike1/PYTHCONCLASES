"""Uso de la libreria datetime"""

from datetime import datetime

dias = ["Lunes", "Martes","Miercoles", "Jueves", "Viernes","Sabado","Domingo"]
"""weekday: Obtendremos el día de la semana de la fecha que estamos enviando como primer parámetro"""
d = datetime.strptime("1990/03/05 20:40:00", "%Y/%m/%d %H:%M:%S")
print("El dia de la semana para esa fecha fue {}".format(dias[d.weekday()]))

