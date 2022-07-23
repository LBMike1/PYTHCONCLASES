from datetime import datetime

strfecha = "08/31/2051"

conversion = datetime.strptime(strfecha, "%m/%d/%Y")

print("La fecha formateada es: {}".format(conversion))

conversion2 = datetime.strftime(conversion," %d de %b del %Y")
"""b: reemaplza a 'm' para representar el mes en string"""
print("La fecha convertida con nuevo formato es: {}".format(conversion2))