"""Estructura de datos"""

"""Listas: hacer una copia de la lista original en otra"""

var1 = ["SQLSERVER", "JDS", "MYHUB", "POSTMOR"]

"usando copy"

var2 = var1.copy()
var2.append("CALLE")
var2.remove("POSTMOR")

print("Mi lista original es: {}".format(var1))
print("La copia de mi lista es: {}".format(var2))