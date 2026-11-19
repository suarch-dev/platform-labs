# import requests
# url = "https://httpbin.org/post"
# with open("servidores.txt", "r") as archivo:
#     for lines in archivo.readlines():
#         if ":" in lines:
#             separado = lines.split(":")
#             # aviso = 
#             # mensaje = separado[1].strip
#             if "DOWN" in separado[1]:
#                 respuesta = requests.post(url, json={"alerta": separado[0].strip()})
#                 print(respuesta.status_code)
#                 print(lines)

# CORRECIONES

# El operador in funcionó de maravilla: Como separado[1] vale "DOWN\n", al poner if "DOWN" in separado[1]:, Python dice "sí, el texto 'DOWN' está dentro de ese string". Funciona perfecto. (Otra opción más estricta sería limpiarlo primero: if separado[1].strip() == "DOWN":, pero tu forma es muy válida).

# Vuelve al for directo: Fíjate que volviste a usar archivo.readlines(). Para este archivo diminuto da igual, pero recuerda el "Pro Tip" de ayer: en producción, para leer logs que pueden pesar gigabytes, es mejor usar for lines in archivo: (sin el readlines). Así no saturas la memoria RAM. Es un detalle que a los entrevistadores les encanta ver.

import requests
url = "https://httpbin.org/post"
with open("servidores.txt", "r") as archivo:
    for lines in archivo:
        if ":" in lines:
            separado = lines.split(":")
            # aviso = 
            # mensaje = separado[1].strip
            if separado[1].strip() == "DOWN":
                respuesta = requests.post(url, json={"alerta": separado[0].strip()})
                print(respuesta.status_code)
                print(lines)