"""uso de la libreria de fechas y tiempos"""

"""Comparacion de fechas"""

import datetime

fecha1 = datetime.datetime(2023, 4, 19) #Tipo de dato datetime
fecha2 = datetime.datetime(2023, 4, 16) #Tipo de dato datetime

if fecha1 == fecha2:
    print("Nacieron el mismo dia")
elif fecha1 < fecha2:
    print("El niño 1 es mayor que el niño 2")
