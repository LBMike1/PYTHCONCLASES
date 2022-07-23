"""Manejo de cadenas"""

cadena = " relacion consensual entre trabajadores"

cadena2 = cadena.replace(cadena[0:8], "gologolo")

print("Cadena con reemplazos tiene el siguiente valor: {}".format(cadena2))

"""Eliminando espacios en blanco antes de mi cadena"""

cadena3 = "          Tremenda saca"
print("El valor original de mi cadena es: {}".format(cadena3))
cadena4 =   cadena3.strip()

print("Cadena con espacios en blanco eliminados tiene el siguiente valor: {}".format(cadena3.strip()))

"""Eliminando espacios en blanco al final de mi cadena"""

cadena5 = "Terrible vacalechera        "

print("El valor de mi cadena con espacios eliminados es : {}".format(cadena5.strip()))
