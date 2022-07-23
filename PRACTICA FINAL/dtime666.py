from datetime import datetime

fecha1 = datetime.strptime("01-07-2000 15:15:00", "%d-%m-%Y %H:%M:%S")
fecha2 = datetime.strptime("01-07-2009 15:15:00", "%d-%m-%Y %H:%M:%S")

tiempo = fecha2 - fecha1

print("La fecha final es : {}".format(tiempo))