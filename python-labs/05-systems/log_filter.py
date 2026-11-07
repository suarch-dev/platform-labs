# with open("log.txt", "r") as archivo:
#     with open("errores.txt", "w") as errores:
#         for linea in archivo:
#             if "ERROR" in linea:
#                 errores.write(linea)

with open("log.txt", "r") as archivo:
    lines = archivo.readlines()
    print(lines[-1])

#el readlines es para CARGAR todo el ARCHIVO en la RAM