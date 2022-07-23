
"""uso de la libreria de fechas y tiempos"""

from datetime import date, time, datetime

fecha = date.today()
print("La fecha a manejar es la siguiente: {}".format(fecha))

tiempo = datetime.now()

print("El tiempo actual es: {}".format(tiempo))

anio = tiempo.year
mes = tiempo.month
dia = tiempo.day

print("El año actual es: {}".format(anio))
print("El mes actual es: {}".format(mes))
print("El dia actual es: {}".format(dia))

"""USo del datetime para extraer la hora, minutos y segundos"""

hora = tiempo.hour      #Obtenemos la hora
minuto = tiempo.minute  #Obtenemos el minuto
segundo = tiempo.second #Obtenemos el segundo

print("La hora exacta son las : {} horas con {} minutos y {} segundos".format(hora, minuto, segundo))