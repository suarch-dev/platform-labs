import requests

url = "https://api.github.com/users/suarch-dev"

try:
    respuesta = requests.get(url)
    print(respuesta.status_code)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        print(datos["public_repos"])
        print(datos["login"])
except Exception as e:
    print(e)