# https://pokeapi.co/api/v2/pokemon/charizard


import requests
#200 = ok
#404 = error de permisos
#500 = Error en el servidor
res =requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

print(res.status_code)
print(res.headers)

json =res.json()
print(json)
