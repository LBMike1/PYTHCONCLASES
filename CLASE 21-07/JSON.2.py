"""Uso de la libreria JSON para traer tipos de data JSON"""

"""IMPORTAMOS DE LA LIBRERIA JSON"""
import json

pythondict = {"nombre": "Juana", "edad": 30, "DNI": "0995412"}

"""CONVERSION DE TIPO DE DATO JSON"""

dicttojson = json.dumps(pythondict)

print("El valor de mi conversion de json a python es: {}".format(dicttojson))
print("El tipo de dato convertido de dict to json es: {}".format(type(dicttojson)))