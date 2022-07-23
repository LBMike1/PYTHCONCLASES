from datetime import datetime

dias = ["Lunes", "Martes","Miercoles", "Jueves", "Viernes","Sabado","Domingo"]

d = datetime.strptime("2023/03/15 20:40:00", "%Y/%m/%d %H:%M:%S")

print("El dia de la semana para esa fecha fue: {}".format(dias[d.weekday()]))