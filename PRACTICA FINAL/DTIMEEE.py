from datetime import date,time, datetime

fecha = date.today()
tiempo = datetime.now()

print("La fecha a manejar es la sigueinte: {}".format(fecha))

print("EL tiempo ahora mismo es: {}".format(tiempo))

anio = date.year
mes = date.month
dia = date.day

hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second
    
print("El tiempo ahora mismo es {} horas, {} minutos y {} segundos".format(hora,minuto,segundo))