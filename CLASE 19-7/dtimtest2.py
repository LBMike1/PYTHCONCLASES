"""uso de la libreria de fechas y tiempos"""

from datetime import datetime

strFecha = "2/6/2023"

conversion = datetime.strptime(strFecha, "%m/%d/%Y")
print("La fecha formateada es : {}".format(conversion))


"TRAER EL MES DE LA FECHA EN FORMATO LETRAS"
conversionmes = datetime.strftime(conversion, "%b %d %Y")
"""b: reemaplza a 'm' para representar el mes"""
print("Nuestra fecha con cambio de mes es el siguiente : {}".format(conversionmes))