equipo = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Carlos", "edad": 25},
    {"nombre": "Beatriz", "edad": 35}
]

# def buscar_mas_joven(equipo):
#     edad = 999
#     nombre_mas_joven = ""
#     for persona in equipo:
#         if persona["edad"] < edad:
#             edad = persona["edad"]
#             nombre_mas_joven = persona["nombre"]
#     return nombre_mas_joven

# print(buscar_mas_joven(equipo))

def find_mas_joven(equipo):
    edad = equipo[0]["edad"]
    mas_joven = equipo[0]["nombre"]
    for persona in equipo:
        if persona["edad"] < edad:
            edad = persona["edad"]
            mas_joven = persona["nombre"]
    return mas_joven

print(find_mas_joven(equipo))