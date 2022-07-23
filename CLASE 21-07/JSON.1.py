"""Uso de la libreria JSON para traer tipos de data JSON"""

"""IMPORTAMOS DE LA LIBRERIA JSON"""
import json

jsonDatos = '{"nombre": "PYTHON", "tipo" : "backend", "paradigma": "Orientado a Objetos"}'

"""convirtiendo a un dato que pueda manejar PYTHON: loads()"""

dictionaryToJson = json.loads(jsonDatos)

print("Imprimir los datos de JSON para PYTHON: {}".format(dictionaryToJson))
print(dictionaryToJson['paradigma'])

print("EL tipo de dato de nuestra variable es: {}".format

