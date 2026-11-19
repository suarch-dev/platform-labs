import requests

url = "https://httpbin.org/post"
#Diccionarios: La API de nuestro simulador espera recibir un JSON con esta estructura exacta:
#{"mensaje": "El texto de la alerta"}

with open("alertas.txt", "r") as archivo:
    for lines in archivo:
        # partes = lines.split(":")
        # mensaje = partes[0].strip()       # 'CRITICAL'
        # descripcion = partes[1].strip()     # 'CPU al 99%'
        if "CRITICAL" in lines:
            respuesta = requests.post(url, json={"mensaje": lines.strip()})
            print(respuesta.status_code)