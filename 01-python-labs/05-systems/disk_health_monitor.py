"""
Vocabulario:
import subprocess
subprocess.run(["comando", "argumento"], capture_output=True, text=True)
capture_output=True: Le dice que "capture" la respuesta del comando.
text=True: Le dice que devuelva el resultado como texto (string) en lugar de bytes.
Para leer el resultado usas: .stdout (la salida normal) o .stderr (los errores).
2. try/except (Programación defensiva)
Qué es: Un bloque para intentar hacer algo (try) y, si falla, hacer otra cosa (except) en lugar de que el programa explote y se cierre.

try:
    # Código que podría fallar (ej: abrir un archivo que no existe)
except Exception as e: 
    # Qué hacer si falla. 'e' guarda el mensaje de error.
3. logging (El sustituto profesional del print)
Qué es: Una librería para registrar eventos. En lugar de print(), los profesionales usan logging. Así puedes guardar los registros en un archivo o mostrarlos con colores según su gravedad.
Vocabulario:
import logging
logging.basicConfig(level=logging.INFO): Configura el nivel mínimo de mensajes que quieres ver.
logging.info("Mensaje de información")
logging.error("Mensaje de error")
logging.warning("Mensaje de advertencia")
"""

import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Iniciando chequeo de disco...")

# try:
#     captura = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
#     solodatos = captura.stdout.split("\n")[1]
#     for dato in solodatos.split(" "):
#         if "%" in dato:
#             valor = int(dato.replace("%", ""))
#             # print(valor)
#             if valor < 80:
#                 logging.warning(f"Alerta. Disco lleno: {valor}")
#     else:
#         logging.info("Todo sano")
# except Exception as e:
#     logging.error(f"error: {e}")

try:
    datos = subprocess.run(["df", "-h", "/"], capture_output=True, text=True).stdout.split("\n")[1].split()
    # datosok = datos.stdout.split("\n")[1].split()
    # valores = datosok.split()
    print(datos[4].strip())
    valor = int(datos[4].strip().replace("%", ""))
    if valor > 80:
        logging.warning(f"Alerta. Disco lleno: {valor}")
    else:
        logging.info("Todo ok")
except Exception as e:
    logging.error(e)