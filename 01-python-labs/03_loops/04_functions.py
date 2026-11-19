###
# 04 - Funciones
# Bloques de codigo reutilizables y parametizables
# para hacer tareas especificas
# ###

import subprocess
subprocess.run("clear")

"""Definicion de una funcion

def nombre_de_la_funcion(parametro1, param2, param3, ...)
    #docstring
    #cuerpo de la función
    return valor_de_retorno # opcional

"""

def saludar():
    print("hola")

saludar()
saludar()
saludar()

# Ejemplo de funcion con parametro

nombre = ""

def saludar_a(nombre): # << es el parametro
    print(f"Hola {nombre}")

saludar_a("nuartek") # << es el argumento
saludar_a("midudev")
saludar_a("Con Mayuscula")

# funciones con mas params

def sumar(a, b):
    suma = a + b
    return suma

print(sumar (2, 3))

# result = sumar (2, 3)
# print(result)

def restar(a, b):
    """Resta dos numeros"""
    return a - b

print(restar.__doc__)

# parametro fijo/por defecto
def multiply(a, b = 2):
    return a * b
print(multiply(3))

# argumentos por posicion

def describir(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

describir("nuartek", 19, "doggy")

# argumentos por clave / params nombrados

describir(sexo="doggy", nombre="nuartek", edad=19)

# args de longitud de variable (*args)

def sumar_num(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_num(1, 2, 3, 10))

def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)
